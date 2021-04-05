from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


# from . import project_worker


# Shared properties
class AccountingTransactionBase(BaseModel):
    id: int = None
    user_id: int = None
    type_id: int = None
    amount: Decimal = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True


class AccountingTransactionCreate(BaseModel):
    user_id: int = None
    type_id: int = None
    amount: Decimal = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True


class AccountingTransactionUpdate(BaseModel):
    id: int = None
    amount: Decimal = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True


class AccountingTransaction(AccountingTransactionBase):
    pass

