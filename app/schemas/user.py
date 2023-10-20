from pydantic import BaseModel, EmailStr
from app.utils import constants


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    user_type: constants.UserType


class UserCreateSchema(UserBaseSchema):
    pass


class UserUpdateSchema(UserBaseSchema):
    pass


class UserResponseSchema(UserBaseSchema):
    pass
