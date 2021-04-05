from typing import TYPE_CHECKING

import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.project_worker import ProjectWorker

if TYPE_CHECKING:
    pass


class AccountingTransactionType(Base):
    __tablename__ = 'accounting_transaction_type'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=False, unique=True)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.current_timestamp())
