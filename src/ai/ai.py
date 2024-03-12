from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from loguru import logger

from config import settings

max_message_history_length = settings.CHAT_MAX_MESSAGE_HISTORY_LENGTH
message_summarization_threshold = settings.CHAT_MESSAGE_HISTORY_SUMMARY_THRESHOLD

chat = ChatOpenAI(model=settings.OPENAI_MODEL, temperature=settings.AI_TEMPERATURE)

ephemeral_chat_history = ChatMessageHistory()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            settings.AI_SYSTEM_ROLE_PROMPT,
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ]
)
chain = prompt | chat

chain_with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: ephemeral_chat_history,  # type: ignore
    input_messages_key="input",
    history_messages_key="chat_history",
)


def summarize_trim_messages(chain_input):
    """
    当聊天记录超过max_message_history_length时，
    只保留最近的max_message_history_length条聊天记录
    同时将max_message_history_length之前的聊天记录进行总结
    :param chain_input:
    :return:
    """
    stored_messages = ephemeral_chat_history.messages
    if len(stored_messages) == 0:
        return False

    # 为避免频繁总计，达到最大长度+阈值之后才会对消息进行一次总结
    if len(stored_messages) <= (max_message_history_length + message_summarization_threshold):
        return False

    summarization_prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="chat_history"),
            (
                "user",
                "将上述聊天消息提炼成一条摘要消息，包含尽可能多的具体细节。",
            ),
        ]
    )
    summarization_chain = summarization_prompt | chat

    need_summary_messages = stored_messages[:-max_message_history_length]

    summary_message = summarization_chain.invoke({"chat_history": need_summary_messages})

    # 重组聊天记录
    ephemeral_chat_history.clear()
    ephemeral_chat_history.add_message(summary_message)
    for message in stored_messages[-max_message_history_length:]:
        ephemeral_chat_history.add_message(message)

    return True


chain_with_summarization_trimming = (
    RunnablePassthrough.assign(messages_summarized=summarize_trim_messages) | chain_with_message_history
)


def chat_with_text(message: str, session_id: str = "unused"):
    ai_message = chain_with_summarization_trimming.invoke(
        {"input": message},
        {"configurable": {"session_id": session_id}},
    )
    logger.debug(ephemeral_chat_history.messages)
    return ai_message.content
