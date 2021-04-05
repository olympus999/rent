from typing import TYPE_CHECKING
import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, \
    ForeignKey, SmallInteger, CheckConstraint, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.project_worker import ProjectWorker
from app.models.project_worker_active import ProjectWorkerActive
# from app.models import ProjectWorkerActive, ProjectWorker
# from app.models import ProjectWorkerActive, ProjectWorker

if TYPE_CHECKING:
    pass


class UserFeedback(Base):
    __tablename__ = 'user_feedback'

    id = Column(Integer, primary_key=True, index=True)
    feedback_given_user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    feedback_received_user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    project_worker_id = Column(Integer, ForeignKey('project_worker.id'), index=True, nullable=False)
    rating = Column(SmallInteger, nullable=False)
    comment = Column(Text)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, nullable=False)

    project_worker = relationship('ProjectWorker')
    feedback_given_user = relationship('User', foreign_keys=[feedback_given_user_id])
    feedback_received_user = relationship('User', foreign_keys=[feedback_received_user_id])

    __table_args__ = (
        CheckConstraint(rating >= 0, name='user_feedback_rating_check_positive'),
        CheckConstraint(rating <= 5, name='user_feedback_rating_check_max_5'),
        UniqueConstraint('feedback_given_user_id',
                         'feedback_received_user_id',
                         'project_worker_id',
                         name='uix_user_feedback_given_and_received_user_id_project_worker_id'),
        {})
