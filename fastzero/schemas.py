from typing import List

from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserList(BaseModel):
    users: List[UserPublic]
