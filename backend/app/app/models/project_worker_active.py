import datetime

from sqlalchemy import Integer, ForeignKey, Column, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ProjectWorkerActive(Base):
    __tablename__ = 'project_worker_active'

    id = Column(Integer, primary_key=True, index=True)
    project_worker_id = Column(Integer, ForeignKey('project_worker.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

    __table_args__ = (
        UniqueConstraint('project_worker_id', 'user_id', name='uix_project_worker_active_user_project_worker'),
    )

    # project_worker = relationship('ProjectWorker')
    worker_active = relationship('User')
    project_worker = relationship('ProjectWorker', uselist=False,)
