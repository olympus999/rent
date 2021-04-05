import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    pass


class AccountingBalance(Base):
    __tablename__ = 'accounting_balance'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False, unique=True)
    balance = Column(Numeric, nullable=False)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.current_timestamp())

    user = relationship('User')
