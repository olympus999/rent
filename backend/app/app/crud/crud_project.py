from typing import Optional, TypeVar, List, Any
import datetime

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session, lazyload, raiseload, joinedload, subqueryload

from app.db.base_class import Base
from app.crud.base import CRUDBase
from app.crud.utils import update_or_create_project
from app.crud import user
from app.models.project_worker import ProjectWorker
from app.models.project_worker_active import ProjectWorkerActive
from app.models.user_feedback import UserFeedback
from app.models.user import User
from app import schemas
from app.models.project import Project
from app.schemas.project import ProjectBase, ProjectCreate, ProjectUpdate


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):

    # noinspection PyMethodOverriding
    def create(self, db: Session, obj_in: ProjectCreate) -> Any:
        db_obj = Project(
            user_id=obj_in.user_id,
            name=obj_in.name,
            address=obj_in.address,
            description=obj_in.description
        )
        db.add(db_obj)
        db.flush()
        db.commit()
        db.refresh(db_obj)
        
        return db_obj

    def get_project_with_workers(self, db: Session, project_id: int, skip: int = 0, limit: int = 500) \
            -> Any:
            # -> schemas.ProjectWithProjectWorker:
        return db.query(self.model) \
            .options(subqueryload(self.model.project_worker)
                     .subqueryload(ProjectWorker.worker)) \
            .filter(Project.id == project_id) \
            .offset(skip) \
            .limit(limit).first()

    def get_many_projects_with_workers(self, db: Session, return_removed: bool = False, skip: int = 0, limit: int = 500) \
            -> Any:
        q = db.query(self.model)
        f = []
        if return_removed:
            f.append(Project.removed_dt.isnot(None))
        else:
            f.append(Project.removed_dt.is_(None))

        return q.options(subqueryload(self.model.project_worker).subqueryload(ProjectWorker.worker)
                         .subqueryload(User.project_worker_active).subqueryload(ProjectWorkerActive.project_worker),
                         subqueryload(self.model.project_worker).subqueryload(ProjectWorker.user_feedback)) \
            .filter(*f) \
            .offset(skip) \
            .limit(limit).all()

    def delete(self, db: Session, project_id: int) -> Any:

        p = self.get_project_with_workers(db, project_id)

        for pw in p.project_worker:
            pw.removed_dt = datetime.datetime.utcnow()

        # Update project to remove all the associated workers
        p = update_or_create_project(db, p)

        # Set project to deleted
        p.removed_dt = datetime.datetime.utcnow()

        db.commit()
        db.refresh(p)

        return p


project = CRUDProject(Project)
