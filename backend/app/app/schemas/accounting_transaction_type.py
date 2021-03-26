from pydantic import BaseModel


# Shared properties
class AccountingTransactionTypeBase(BaseModel):
    id: int = None
    name: str = None

    class Config:
        orm_mode = True


class AccountingTransactionTypeCreate(AccountingTransactionTypeBase):
    pass


class AccountingTransactionTypeUpdate(AccountingTransactionTypeBase):
    pass


class AccountingTransactionType(AccountingTransactionTypeBase):
    pass
