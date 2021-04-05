from typing import Optional, List
import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class UserToolBase(BaseModel):
    user_id: int = None
    tool_id: int = None
    details: Optional[str] = None

    class Config:
        orm_mode = True


class UserToolCreate(UserToolBase):
    pass


class UserToolUpdate(UserToolBase):
    id: int = None
    pass


class UserToolWithToolDetails(UserToolBase):
    id: int = None
    tool: "Tool"


class UserTool(UserToolBase):
    pass


from .tool import Tool
UserToolWithToolDetails.update_forward_refs()
