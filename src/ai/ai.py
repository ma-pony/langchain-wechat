from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from config import settings

chat = ChatOpenAI(
    model=settings.OPENAI_MODEL,
    temperature=settings.AI_TEMPERATURE
)

ephemeral_chat_history = ChatMessageHistory(

)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            settings.AI_SYSTEM_PROMPT,
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


def chat_with_text(message: str):
    ephemeral_chat_history.add_user_message(message)
    chain = prompt | chat

    ai_message = chain.invoke(
        {
            "messages": ephemeral_chat_history.messages,
        }
    )
    ephemeral_chat_history.add_ai_message(ai_message.content)
    return ai_message.content
