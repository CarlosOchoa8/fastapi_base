"""
Settings for the project.
"""

# Imports
from pydantic import Extra
from pydantic_settings import BaseSettings

from app.config.common import CONFIG_FILE, AppSettings
# Settings class imports
from app.config.database.settings import DatabaseSettings
from app.config.auth.settings import AuthSettings


class Settings(BaseSettings):
    """
    Settings class for the project.
    """

    app_environment: str
    database: AppSettings = DatabaseSettings()
    auth: AppSettings = AuthSettings()

    class Config:
        """
        Settings class configuration.
        """

        env_file = CONFIG_FILE
        extra = Extra.allow


settings = Settings()
a = Settings()
