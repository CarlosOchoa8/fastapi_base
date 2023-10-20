#!/usr/bin/env python3
"""
Database Handler
"""
from os import getenv

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.database.config import get_postgres_uri

# engine = get_postgres_uri()
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=create_engine(
#         engine,
#         isolation_level="REPEATABLE READ",
#     ),
# )
#
# Base = declarative_base()

engine = get_postgres_uri()
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(
        engine,
        isolation_level="REPEATABLE READ"
    ),
)

Base = declarative_base()
