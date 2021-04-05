import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    pass


class AccountingTransaction(Base):
    __tablename__ = 'accounting_transaction'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    type_id = Column(Integer, ForeignKey('accounting_transaction_type.id'), index=True, nullable=False)
    amount = Column(Numeric, nullable=False)
    comment = Column(String)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

    user = relationship('User')
