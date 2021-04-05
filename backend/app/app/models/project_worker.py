import datetime

from sqlalchemy import Integer, ForeignKey, Column, DateTime, Boolean, UniqueConstraint
from sqlalchemy import func
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ProjectWorker(Base):
    __tablename__ = 'project_worker'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.current_timestamp())
    removed_dt = Column(DateTime(timezone=True))
    
    worker_accepted_dt = Column(DateTime(timezone=True))
    worker_rejected_dt = Column(DateTime(timezone=True))
    show_project_to_worker = Column(Boolean, default=True)
    __table_args__ = (
        UniqueConstraint('project_id', 'user_id', name='uix_project_worker_user_project'),
    )
    
    worker = relationship('User')
    project = relationship('Project')
    user_feedback = relationship('UserFeedback', uselist=False)
    project_worker_active = relationship('ProjectWorkerActive', cascade="all, delete-orphan")
