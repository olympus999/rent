from typing import Any, Dict, Optional, Union, List
from app.crud.base import CRUDBase
from app.models.accounting_balance import AccountingBalance
from app.schemas.accounting_balance import AccountingBalanceCreate, AccountingBalanceUpdate
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from decimal import Decimal
from app import crud
import numpy as np


class CRUDAccountingBalance(CRUDBase[AccountingBalance, AccountingBalanceCreate, AccountingBalanceUpdate]):

    def create_0_balance(self, db: Session, user_id: int, commit: bool = True):
        obj_in = AccountingBalanceCreate(user_id=user_id, balance=0)
        db_obj = self.create(db, obj_in=obj_in)
        if commit:
            db.add(db_obj)
            db.commit()
        return db

    def get_by_user_id(self, db: Session, user_id: int):
        db_obj = db.query(AccountingBalance)\
            .filter(self.model.user_id == user_id).first()
        if not db_obj:
            self.create_0_balance(db, user_id)
            db_obj = self.get_by_user_id(db, user_id)
        return db_obj

    # noinspection PyMethodOverriding
    def update(self,
               db: Session,
               user_id: int,
               add: Decimal,
               commit: bool = True):
        add = Decimal(add)
        db_obj = self.get_by_user_id(db, user_id)
        # If Balance object does not exist, create one
        if not db_obj:
            db = self.create_0_balance(db, user_id, commit=False)

        db_obj.balance = db_obj.balance + add
        db.add(db_obj)
        if commit:
            db.commit()
        return db

    def recalculate_balance(self, db: Session, user_id: int):
        transactions = crud.accounting_transaction.get_by_user_id(db, user_id)
        hours = crud.accounting_hour.get_by_user_id(db, user_id)
        db_obj = self.get_by_user_id(db, user_id)

        total_transactions_amount = np.sum([x.amount for x in transactions])
        total_hours_amount = np.sum([x.hour_count*x.per_hour_cost for x in hours])

        db_obj.balance = total_hours_amount + total_transactions_amount
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj


accounting_balance = CRUDAccountingBalance(AccountingBalance)
