from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class UserFeedbackBase(BaseModel):
    feedback_given_user_id: int = None
    feedback_received_user_id: int = None
    project_worker_id: int = None
    rating: int = None
    comment: str = None
    created_dt: datetime = None
    
    
class UserFeedbackCreate(UserFeedbackBase):
    class Config:
        orm_mode = True


class UserFeedbackUpdate(UserFeedbackBase):
    id: int = None
    
    class Config:
        orm_mode = True


class UserFeedbackWithProject(UserFeedbackBase):
    project_worker: "project_worker.ProjectWorkerProject"

    class Config:
        orm_mode = True


class UserFeedback(UserFeedbackUpdate):
    pass


from . import project_worker
from . import project_worker_active
UserFeedbackWithProject.update_forward_refs()
