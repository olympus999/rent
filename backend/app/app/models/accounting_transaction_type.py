import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, DateTime, func

from app.db.base_class import Base

if TYPE_CHECKING:
    pass


class AccountingTransactionType(Base):
    __tablename__ = 'accounting_transaction_type'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=False, unique=True)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.current_timestamp())
