from typing import TYPE_CHECKING

import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.assocations.project_worker import ProjectWorkers

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    name = Column(String)
    address = Column(String)
    description = Column(String)
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime, default=datetime.datetime.utcnow)

    workers = relationship('User', secondary=ProjectWorkers, back_populates="project_worker")
