from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProjectWorkerBase(BaseModel):
    project_id: int = None
    user_id: int = None
    created_dt: datetime = None
    modified_dt: datetime = None
    removed_dt: datetime = None
    worker_accepted_dt: datetime = None
    worker_rejected_dt: datetime = None
    show_project_to_worker: bool = None

    class Config:
        orm_mode = True


class ProjectWorkerAdminBase(BaseModel):
    id: int = None
    created_dt: datetime = None
    modified_dt: datetime = None
    removed_dt: datetime = None
    worker_accepted_dt: datetime = None
    worker_rejected_dt: datetime = None
    show_project_to_worker: bool = None

    class Config:
        orm_mode = True


class ProjectWorkerProjectAdmin(ProjectWorkerAdminBase):
    project: "ProjectWithUser"
    

class ProjectWorkerAdminCreateUpdate(BaseModel):
    id: int = None
    removed_dt: datetime = None
    worker_accepted_dt: datetime = None
    worker_rejected_dt: datetime = None
    show_project_to_worker: bool = None
    worker: "WorkerAdmin"

    class Config:
        orm_mode = True


class ProjectWorkerWithWorkerAndUserFeedback(BaseModel):
    id: int = None
    removed_dt: datetime = None
    worker_accepted_dt: datetime = None
    worker_rejected_dt: datetime = None
    show_project_to_worker: bool = None
    worker: "WorkerAdmin"
    user_feedback: Optional["UserFeedback"]

    class Config:
        orm_mode = True


class ProjectWorkerAdmin(ProjectWorkerAdminBase):
    worker: "WorkerAdmin"
    project_worker_active: "ProjectWorkerActiveBase"

    class Config:
        orm_mode = True


class ProjectWorkerProject(BaseModel):
    project: "Project"

    class Config:
        orm_mode = True


from .user_feedback import UserFeedback
from .project import ProjectWithUser, Project
from .user import WorkerAdmin
from .project_worker_active import ProjectWorkerActiveBase
ProjectWorkerProjectAdmin.update_forward_refs()
ProjectWorkerAdminCreateUpdate.update_forward_refs()
ProjectWorkerAdmin.update_forward_refs()
ProjectWorkerWithWorkerAndUserFeedback.update_forward_refs()
ProjectWorkerProject.update_forward_refs()
