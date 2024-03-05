from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from config import settings


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


def start_channel():
    pass


app = FastAPI(title=settings.PROJECT_NAME)

app.add_event_handler("startup", start_channel)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
