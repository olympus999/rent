from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, EmailStr
# from . import project_worker


# Shared properties
class ToolBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class ToolCreate(ToolBase):
    pass


class ToolUpdate(ToolBase):
    id: int = None


class Tool(ToolBase):
    id: int = None
    modified_dt: datetime = None
    created_dt: datetime = None
