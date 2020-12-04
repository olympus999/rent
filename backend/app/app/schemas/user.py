from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    available: Optional[bool] = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class Worker(BaseModel):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
    first_name: Optional[str] = None
    available: Optional[bool] = False

    class Config:
        orm_mode = True
