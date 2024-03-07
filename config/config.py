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
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    OPENAI_API_KEY: str = "sk-1234567890"

    # itchat
    WECHAT_HOT_RELOAD: bool = False
    WECHAT_USER_DATA_STORAGE_PATH: str = "storage"
