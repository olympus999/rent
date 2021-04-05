from typing import Any, Dict, Optional, Union, List
from app.crud.base import CRUDBase
from app.models.accounting_transaction import AccountingTransaction
from app.schemas.accounting_transaction import AccountingTransactionCreate, AccountingTransactionUpdate
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app import crud


class CRUDAccountingTransaction(CRUDBase[AccountingTransaction, AccountingTransactionCreate, AccountingTransactionUpdate]):

    def create(self, db: Session, *, obj_in: AccountingTransactionCreate):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)

        db = crud.accounting_balance.update(db, obj_in.user_id, obj_in.amount, commit=False)

        db.commit()
        db.refresh(db_obj)

        return db_obj

    def get_by_user_id(self, db: Session, user_id: int) -> List[AccountingTransaction]:
        return db.query(self.model).filter(self.model.user_id == user_id).all()


accounting_transaction = CRUDAccountingTransaction(AccountingTransaction)
