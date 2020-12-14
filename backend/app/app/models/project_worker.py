import datetime
from sqlalchemy import Integer, ForeignKey, Table, Column, DateTime, String, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ProjectWorkers(Base):
    __tablename__ = 'project_worker'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime, default=datetime.datetime.utcnow)
    
    worker_accepted_dt = Column(DateTime)
    worker_rejected_dt = Column(DateTime)
    show_project_to_worker = Column(Boolean, default=True)
    __table_args__ = (
        UniqueConstraint('project_id', 'user_id', name='uix_project_worker_user_project'),
    )
    
    worker = relationship('User', lazy='joined')
