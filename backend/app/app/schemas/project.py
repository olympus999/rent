from typing import Optional, List

from pydantic import BaseModel
from .user import Worker


class ProjectBase(BaseModel):
    user_id: int = None
    name: str = None
    address: str = None
    description: str = None
    workers: List[Worker]


class ProjectCreate(ProjectBase):

    class Config:
        orm_mode = True


# class ProjectCreateIncludeWorkers(ProjectCreate):
#     workers: List[Worker]


class ProjectUpdate(ProjectCreate):
    pass


class Project(ProjectBase):
    pass
