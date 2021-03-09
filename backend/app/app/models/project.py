from typing import TYPE_CHECKING

import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.project_worker import ProjectWorker

if TYPE_CHECKING:
    pass


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    name = Column(String)
    address = Column(String)
    description = Column(String)
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime, default=datetime.datetime.utcnow, onupdate=func.current_timestamp())
    removed_dt = Column(DateTime)

    workers = relationship('User', secondary=ProjectWorker.__tablename__, back_populates="project_worker")
    project_worker = relationship('ProjectWorker')
    client = relationship('User')
