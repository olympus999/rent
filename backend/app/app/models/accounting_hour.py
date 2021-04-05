import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Date, func, Numeric, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    pass


class AccountingHour(Base):
    __tablename__ = 'accounting_hour'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    day = Column(Date, nullable=False)
    hour_count = Column(Numeric, nullable=False)
    per_hour_cost = Column(Numeric, nullable=False)
    comment = Column(String)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.current_timestamp())

    __table_args__ = (
        UniqueConstraint('user_id', 'day', name='uix_accounting_hour_user_id_day'),
    )

    user = relationship('User')
    project = relationship('Project')
