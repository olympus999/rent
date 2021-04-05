from typing import Optional, List
import datetime

from pydantic import BaseModel, EmailStr
# from . import project_worker


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


class UserInfo(BaseModel):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    available: Optional[bool] = False
    project_worker_active: Optional["project_worker_active.ProjectWorkerActiveProjectActive"]
    user_feedback: Optional["List[user_feedback.UserFeedbackWithProject]"]
    average_rating: Optional[float] = None
    show_available: Optional[bool] = False

    class Config:
        orm_mode = True


class WorkerAdmin(BaseModel):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    available: Optional[bool] = False
    project_worker_active: Optional["project_worker_active.ProjectWorkerActiveProject"]

    class Config:
        orm_mode = True


class WorkerActiveAdmin(BaseModel):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    available: Optional[bool] = False
    project_worker_active: Optional["project_worker_active.ProjectWorkerActiveProjectActive"]
    user_feedback: Optional["List[user_feedback.UserFeedbackWithProject]"]
    average_rating: Optional[float] = None
    show_available: Optional[bool] = False

    class Config:
        orm_mode = True


class WorkerAvailableAdmin(BaseModel):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    available: Optional[bool] = False

    class Config:
        orm_mode = True


class Worker(BaseModel):
    id: Optional[int] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
    first_name: Optional[str] = None
    available: Optional[bool] = False

    class Config:
        orm_mode = True


from . import user_feedback
from . import project_worker_active
UserInfo.update_forward_refs()
WorkerAdmin.update_forward_refs()
WorkerActiveAdmin.update_forward_refs()
