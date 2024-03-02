from langchain_openai import ChatOpenAI

from config import settings
from langchain_core.messages import HumanMessage


def main():
    chat = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        model_name=settings.OPENAI_MODEL,
    )
    chat.invoke(
        [
            HumanMessage(
                content="Translate this sentence from English to French: I love programming."
            )
        ]
    )


if __name__ == '__main__':
    main()
