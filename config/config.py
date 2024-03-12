import os
from typing import Tuple, Type

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), ".env"),
        env_file_encoding="utf-8",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return dotenv_settings, env_settings, init_settings, file_secret_settings

    PROJECT_NAME: str = "Langchain Wechat"

    DEBUG: bool = False

    # openai
    OPENAI_MODEL: str = "gpt-3.5-turbo-1106"  # openai模型
    OPENAI_API_KEY: str = "sk-1234567890"  # openai api key

    # AI
    AI_TEMPERATURE: float = 0.5  # AI温度
    AI_SYSTEM_ROLE_PROMPT: str = "你是一个有用的助手,尽你所能回答所有问题."  # AI系统角色提示词

    # 聊天记录
    CHAT_MAX_MESSAGE_HISTORY_LENGTH: int = 10  # 聊天记录最大长度
    CHAT_MESSAGE_HISTORY_SUMMARY_THRESHOLD: int = 5  # 聊天记录总结阈值

    # itchat
    WECHAT_HOT_RELOAD: bool = False  # 是否热重载
    WECHAT_USER_DATA_STORAGE_PATH: str = "storage"  # 用户数据存储路径
