from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.project_worker import ProjectWorker
from app.models.user_feedback import UserFeedback
from app.models.project_worker_active import ProjectWorkerActive
# from app.models import ProjectWorkerActive, ProjectWorker
# from app.models import ProjectWorkerActive, ProjectWorker

if TYPE_CHECKING:
    pass


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    role = Column(String, ForeignKey('user_role.name'))
    available = Column(Boolean, default=True, server_default='1', nullable=False)
    items = relationship("Item", back_populates="owner")

    project = relationship('Project')

    project_worker = relationship('Project', secondary=ProjectWorker.__tablename__, back_populates="workers")
    project_worker_active = relationship('ProjectWorkerActive',
                                         uselist=False,)
    
    user_feedback = relationship('UserFeedback', foreign_keys=UserFeedback.feedback_received_user_id)
