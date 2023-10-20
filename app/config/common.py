"""
Base settings for all apps
"""
from pydantic import Extra
from pydantic_settings import BaseSettings

CONFIG_FILE = ".env"


class AppSettings(BaseSettings):
    class Config:
        env_file = CONFIG_FILE
        extra = Extra.forbid
