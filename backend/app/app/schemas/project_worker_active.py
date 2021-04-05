from typing import Optional, List

from pydantic import BaseModel
from datetime import datetime


class ProjectWorkerActiveBase(BaseModel):
    id: int = None
    project_worker_id: int = None
    user_id: int = None
    created_dt: datetime = None

    class Config:
        orm_mode = True


class ProjectWorkerActiveProject(ProjectWorkerActiveBase):
    project_worker: "project_worker.ProjectWorkerProject"
    pass


class ProjectWorkerActiveProjectActive(ProjectWorkerActiveBase):
    project_worker: "project_worker.ProjectWorkerProjectAdmin"

    class Config:
        orm_mode = True


from . import project_worker
ProjectWorkerActiveProject.update_forward_refs()
ProjectWorkerActiveProjectActive.update_forward_refs()
