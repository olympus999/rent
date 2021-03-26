from app.crud.base import CRUDBase
from app.models.accounting_transaction_type import AccountingTransactionType
from app.schemas.accounting_transaction_type import AccountingTransactionTypeCreate, AccountingTransactionTypeUpdate


class CRUDAccountingTransactionType(CRUDBase[AccountingTransactionType, AccountingTransactionTypeCreate, AccountingTransactionTypeUpdate]):
    pass


accounting_transaction_type = CRUDAccountingTransactionType(AccountingTransactionType)
