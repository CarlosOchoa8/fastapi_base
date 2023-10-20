from typing import Any

from pydantic import BaseModel, EmailStr, field_validator
from app.utils import constants


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    user_type: constants.UserType
    phone_number: str

    @field_validator('first_name', 'last_name')
    def std_name(cls, value: Any) -> BaseModel:
        value = value.capitalize()
        return value.strip()

    @field_validator('phone_number')
    def stp_phone(cls, value: Any) -> BaseModel:
        return value.strip()


class UserCreateSchema(UserBaseSchema):
    pass


class UserUpdateSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone_number: str | None = None


class UserResponseSchema(UserBaseSchema):
    pass
