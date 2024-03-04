from langchain_openai import ChatOpenAI

from config import settings
from langchain_core.messages import HumanMessage


def main():
    chat = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        model_name=settings.OPENAI_MODEL,
    )
    res = chat.invoke(
        [
            HumanMessage(
                content="Translate this sentence from English to French: I am programming."
            )
        ]
    )

    print(res)


if __name__ == '__main__':
    main()
