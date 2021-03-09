from typing import Any, Dict, Optional, Union, List
from app.crud.base import CRUDBase
from app.models.user_tool import UserTool
from app.schemas.user_tool import UserToolCreate, UserToolUpdate
from sqlalchemy.orm import Session, subqueryload


class CRUDUserTool(CRUDBase[UserTool, UserToolCreate, UserToolUpdate]):

    def get_by_user_id(self, db: Session, user_id: int) -> Any:
        return db.query(UserTool)\
            .options(subqueryload(self.model.tool))\
            .filter(UserTool.user_id == user_id)\
            .all()
    pass


user_tool = CRUDUserTool(UserTool)
