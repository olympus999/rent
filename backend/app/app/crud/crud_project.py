from typing import Optional, TypeVar, List, Any

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base
from app.crud.base import CRUDBase
from app.crud import user
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectBase, ProjectCreate, ProjectUpdate


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):

    # noinspection PyMethodOverriding
    def create(self, db: Session, obj_in: ProjectCreate, user_id: int) -> Any:
        db_obj = Project(
            user_id=user_id,
            name=obj_in.name,
            address=obj_in.address,
            description=obj_in.description
        )
        db.add(db_obj)
        db.flush()
        d = jsonable_encoder(obj_in).copy()
        worker_ids = [x['id'] for x in d['workers']]
        user_workers = user.get_workers_by_id(db, worker_ids)
        db_obj.workers.extend(user_workers)
        user.set_workers_unavailable(db, worker_ids)
        db.commit()
        db.refresh(db_obj)

    def get_multi_for_client(self, db: Session, user_id: int, skip: int = 0, limit: int = 500):
        return db.query(Project).filter(Project.id == user_id).offset(skip)\
            .limit(limit).all()

    # def get_mult_for_worker(self, db: Session, user_id: int, skip: int = 0, limit: int = 500):
    #     return db.query(Project).filter(Project.id == user_id).offset(skip)\
    #         .limit(limit).all()




project = CRUDProject(Project)
