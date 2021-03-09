from typing import Optional, List

from pydantic import BaseModel
from datetime import datetime
from .project_worker import ProjectWorkerAdmin, ProjectWorkerAdminCreateUpdate
from .project_worker_active import ProjectWorkerActiveBase


class ProjectAdminCreateUpdate(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    name: Optional[str]
    address: Optional[str]
    description: Optional[str]
    project_worker: Optional[List["ProjectWorkerAdminCreateUpdate"]]

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    user_id: int = None
    name: str = None
    address: str = None
    description: str = None


class ProjectWithUser(ProjectBase):
    id: int = None
    client: "User"

    class Config:
        orm_mode = True


class ProjectCreate(ProjectBase):
    
    class Config:
        orm_mode = True


class ProjectUpdate(BaseModel):
    user_id: Optional[int] = None
    name: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class Project(ProjectBase):
    id: int = None

    class Config:
        orm_mode = True


class ProjectWithProjectWorker(BaseModel):
    id: int = None
    user_id: int = None
    name: str = None
    address: str = None
    description: str = None
    modified_dt: datetime = None
    created_dt: datetime = None
    removed_dt: datetime = None
    project_worker: List["ProjectWorkerWithWorkerAndUserFeedback"]
    
    class Config:
        orm_mode = True


class ProjectWorkerDetailedUpdate(BaseModel):
    user_id: Optional[int] = None
    name: str = None
    address: str = None
    description: str = None
    project_worker: List["ProjectWorkerAdmin"]

    class Config:
        orm_mode = True


from .user import Worker, User
from .project_worker import ProjectWorkerAdmin, ProjectWorkerAdminCreateUpdate, ProjectWorkerWithWorkerAndUserFeedback
from .project_worker_active import ProjectWorkerActiveBase
ProjectWithUser.update_forward_refs()
ProjectAdminCreateUpdate.update_forward_refs()
ProjectWithProjectWorker.update_forward_refs()
ProjectWorkerDetailedUpdate.update_forward_refs()
