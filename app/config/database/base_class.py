"""
  Generate the base of tables
"""

import re
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """Produce a declarative base class.

    Model object with default attributes.

    Attributes:

      - id (Any): model identifier.
      - `__tablename__` (str): auto generated table name from model name

    """

    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generate __tablename__ automatically from the class name and converto to snake case
        """
        return _to_snake_case(cls.__name__)


def _to_snake_case(camel_str: str):
    """
    Convert camel case string to snake_case

      Args:

        camel_str (str, required): CamelCase string to be converted.
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()
