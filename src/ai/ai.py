from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.schema import (
    SystemMessage,
)
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from loguru import logger

from config import settings
from src.ai.tools.date import get_current_date, get_current_datetime

wrapper = DuckDuckGoSearchAPIWrapper(region="cn-zh", max_results=10)
search = DuckDuckGoSearchResults(api_wrapper=wrapper)

max_message_history_length = settings.CHAT_MAX_MESSAGE_HISTORY_LENGTH
message_summarization_threshold = settings.CHAT_MESSAGE_HISTORY_SUMMARY_THRESHOLD


tools = [
    Tool(
        name="Search",
        func=search.run,
        description="当您需要回答有关时事的问题时很有用",
    ),
    Tool(
        name="CurrentDate",
        func=get_current_date,
        description="需要获取当前日期的时候很有用",
    ),
    Tool(
        name="CurrentDatetime",
        func=get_current_datetime,
        description="需要获取当前时间的时候很有用",
    ),
]


def get_message_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(session_id, url=settings.REDIS_URL)


class ChatAgent:
    def __init__(
        self,
        session_id: str,
        system_message: SystemMessage = settings.AI_SYSTEM_ROLE_PROMPT,
    ):
        self.chat = ChatOpenAI(model=settings.OPENAI_MODEL, temperature=settings.AI_TEMPERATURE)
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    system_message,
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        agent = create_openai_tools_agent(self.chat, tools, prompt)

        self.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        self.session_id = session_id
        self.ephemeral_chat_history = get_message_history(session_id)

        self.chain_with_message_history = RunnableWithMessageHistory(
            self.agent_executor,
            get_message_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )

    def summarize_trim_messages(self, chain_input):
        """
        当聊天记录超过max_message_history_length时，
        只保留最近的max_message_history_length条聊天记录
        同时将max_message_history_length之前的聊天记录进行总结
        :param chain_input:
        :return:
        """
        stored_messages = self.ephemeral_chat_history.messages
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
        summarization_chain = summarization_prompt | self.chat

        need_summary_messages = stored_messages[:-max_message_history_length]

        summary_message = summarization_chain.invoke({"chat_history": need_summary_messages})

        # 重组聊天记录
        self.ephemeral_chat_history.clear()
        self.ephemeral_chat_history.add_message(summary_message)
        for message in stored_messages[-max_message_history_length:]:
            self.ephemeral_chat_history.add_message(message)

        return True

    def step(
        self,
        input_message: str,
    ) -> AIMessage:
        # # `messages_summarized`可以是任何字符，只要它是一个有效的变量名
        chain_with_summarization_trimming = (
            RunnablePassthrough.assign(messages_summarized=self.summarize_trim_messages)
            | self.chain_with_message_history
        )

        ai_message = chain_with_summarization_trimming.invoke(
            {"input": input_message},
            {"configurable": {"session_id": self.session_id}},
        )
        logger.debug(self.ephemeral_chat_history.messages)
        return ai_message


def chat_with_text(message: str, session_id: str = "unused"):
    chat_agent = ChatAgent(session_id)
    ai_message = chat_agent.step(message)
    return ai_message["output"]
