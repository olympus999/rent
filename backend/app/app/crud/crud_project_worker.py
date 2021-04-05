from typing import List

from sqlalchemy.orm import Session, subqueryload

from app.crud.base import CRUDBase
from app.models.project_worker import ProjectWorker
from app.schemas.project_worker import ProjectWorkerBase


class CRUDProjectWorker(CRUDBase[ProjectWorker, ProjectWorkerBase, ProjectWorkerBase]):

    def get_project_workers(self, db: Session, project_id: int) \
            -> List[ProjectWorkerBase]:
        return db.query(self.model)\
            .filter(self.model.id == project_id)\
            .all()

    def projects_associated_with_user(self, db: Session, user_id: int):
        return db.query(self.model)\
            .options(subqueryload(self.model.project))\
            .filter(self.model.user_id == user_id).all()

    # def get_specific_project_workers(self, db: Session, project_id: int, _id: Union[List, int]) \
    #         -> List[ProjectWorkerBase]:
    #     return db.query(self.model)\
    #         .filter(self.model.project_id == project_id, self.model.user_id.in_(id_to_list(_id)))\
    #         .all()


project_worker = CRUDProjectWorker(ProjectWorker)
