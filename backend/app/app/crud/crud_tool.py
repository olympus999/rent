from typing import Any, Dict, Optional, Union, List
from app.crud.base import CRUDBase
from app.models.tool import Tool
from app.schemas.tool import ToolCreate, ToolUpdate
from sqlalchemy.orm import Session


class CRUDUser(CRUDBase[Tool, ToolCreate, ToolUpdate]):

    def get_by_name(self, db: Session, name: str) -> Optional[Tool]:
        return db.query(Tool).filter(Tool.name == name).first()


tool = CRUDUser(Tool)
