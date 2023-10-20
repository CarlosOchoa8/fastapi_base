from app.config.database.base_class import Base
from sqlalchemy import Column, String, Integer
from pydantic import Field


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    user_type = Column(String, nullable=False)
