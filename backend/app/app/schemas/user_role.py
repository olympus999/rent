from typing import Optional

from pydantic import BaseModel


class UserRoleBase(BaseModel):
    name: Optional[str] = None


class UserRoleCreate(UserRoleBase):
    id: int

    class Config:
        orm_mode = True


class UserRoleUpdate(UserRoleCreate):
    pass


class UserRole(UserRoleCreate):
    pass
