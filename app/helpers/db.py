from typing import Generator

# from app.config.database.session import SessionLocal
from app.config.database.connection import SessionLocal


def get_db() -> Generator:
    """Get a DB session

    Yields:
        Generator: A sessionmaker instance
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
