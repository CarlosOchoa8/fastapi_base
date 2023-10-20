"""
Settings for database connections
"""
from app.config.common import AppSettings


class DatabaseSettings(AppSettings):
    """
    Database settings
    """
    host: str = "127.0.0.1"
    port: int = 5432
    password: str = "postgres"
    user: str = "postgres"
    name: str = "axios_core"

    @property
    def postgres_uri(self):
        """
        Return the postgres uri
        """
        return self.database_url

    @property
    def database_url(self):
        """
        Return the database url
        """
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}?sslmode=disable"

    class Config:
        """ Subclasses of Config to set prefix """
        env_prefix = "db_"
