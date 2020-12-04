from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def id_to_list(_id):
    return _id if type(_id) is list else [_id]


def workers(db: Session):
    return db.query(User).filter(User.role == 'worker')


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    
    def get_workers(self, db: Session, *, skip: int = 0, limit: int = 500) -> List[User]:
        return workers(db)\
            .with_entities(User.id, User.first_name, User.role, User.available)\
            .offset(skip).limit(limit).all()

    def get_workers_by_id(self, db: Session, _id: Union[List, int]) -> List[User]:
        return workers(db).filter(User.id.in_(id_to_list(_id))).all()

    def update_workers_available_status(self, db: Session, _id: Union[List, int], status: bool) -> List[User]:
        return workers(db).filter(User.id.in_(id_to_list(_id))).update({'available': status}, synchronize_session=False)

    def set_workers_unavailable(self, db: Session, _id: Union[List, int]) -> List[User]:
        return self.update_workers_available_status(db, _id, status=False)

    def set_workers_available(self, db: Session, _id: Union[List, int]) -> List[User]:
        return self.update_workers_available_status(db, _id, status=True)
    
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            role=obj_in.role,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=False)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_worker(self, user: User) -> bool:
        return user.role == 'worker'

    def is_client(self, user: User) -> bool:
        return user.role == 'client'

    def is_superuser(self, user: User) -> bool:
        return user.role == 'superuser'


user = CRUDUser(User)
