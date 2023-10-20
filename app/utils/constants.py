from enum import Enum


class UserType(str, Enum):
    INSTRUCTOR = 'INSTRUCTOR'
    STUDENT = 'STUDENT'
