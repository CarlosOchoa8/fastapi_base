"""
Database handler
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings


SQL_ALCHEMY_DATABASE_URI = settings.database.postgres_uri
engine = create_engine(
    SQL_ALCHEMY_DATABASE_URI,
    isolation_level="REPEATABLE READ"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
