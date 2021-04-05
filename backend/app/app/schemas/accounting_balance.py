from decimal import Decimal

from pydantic import BaseModel


# from . import project_worker


# Shared properties
class AccountingBalanceBase(BaseModel):
    user_id: int = None
    balance: Decimal = 0

    class Config:
        orm_mode = True


class AccountingBalanceCreate(AccountingBalanceBase):
    pass


class AccountingBalanceUpdate(AccountingBalanceBase):
    id: int = None
    pass


class AccountingBalance(AccountingBalanceBase):
    pass
