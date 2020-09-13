from typing import Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base
from app.crud.base import CRUDBase
from app.models.user_role import UserRole
from app.schemas.user_role import UserRoleCreate, UserRoleUpdate

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDUserRole(CRUDBase[UserRole, UserRoleCreate, UserRoleUpdate]):

    def get_all(self, db: Session) -> Optional[ModelType]:
        return db.query(self.model).all()


user_role = CRUDUserRole(UserRole)
