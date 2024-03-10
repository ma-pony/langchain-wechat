from fastapi import FastAPI

from config import settings
from src.wechat import start_channel

app = FastAPI(title=settings.PROJECT_NAME)

app.add_event_handler(
    "startup", start_channel
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
