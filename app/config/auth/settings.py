"""
Settings for the auth app.
"""

from app.config.common import AppSettings


class AuthSettings(AppSettings):
    """
    Auth settings
    """

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config(AppSettings.Config):
        """ Settings class configuration. """

        env_prefix = "auth_"
