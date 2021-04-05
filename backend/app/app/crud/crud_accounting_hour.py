from typing import Any, Dict, Optional, Union, List
from app.crud.base import CRUDBase
from app.models.accounting_hour import AccountingHour
from app.schemas.accounting_hour import AccountingHourCreate, AccountingHourUpdate, AccountingHourCreateOrUpdate
from sqlalchemy.orm import Session, subqueryload
from sqlalchemy import Date
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends, HTTPException
from app import crud
import numpy as np


class CRUDAccountingHour(CRUDBase[AccountingHour, AccountingHourCreate, AccountingHourUpdate]):

    def create_or_update_multi(self, db: Session, _in: List[AccountingHourCreateOrUpdate]):
        # Make sure all changes are for one user only
        assert np.unique([x.user_id for x in _in]).size == 1
        # print("obj_in", jsonable_encoder(_in))
        for obj_in in _in:
            if obj_in.id is None:
                accounting_hour_create = AccountingHourCreate(
                    user_id=obj_in.user_id,
                    project_id=obj_in.project_id,
                    day=obj_in.day,
                    hour_count=obj_in.hour_count,
                    per_hour_cost=obj_in.per_hour_cost,
                    comment=obj_in.comment
                )
                db = self.create(db, accounting_hour_create, commit=False)
            else:
                accounting_hour_update = AccountingHourUpdate(
                    id=obj_in.id,
                    project_id=obj_in.project_id,
                    hour_count=obj_in.hour_count,
                    per_hour_cost=obj_in.per_hour_cost,
                    comment=obj_in.comment
                )
                # print('accounting_hour_update', accounting_hour_update)
                db = self.update(db, accounting_hour_update, commit=False)
        db.commit()
        self.remove_0_balance(db, commit=True)
        return True

    def remove_0_balance(self, db: Session, commit=True):
        db.query(self.model).filter(self.model.hour_count == 0).delete()
        if commit:
            db.commit()
        return db

    # noinspection PyMethodOverriding
    def create(self, db: Session, obj_in: AccountingHourCreate, commit: bool = True):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        print(jsonable_encoder(db_obj))
        db.add(db_obj)

        amount = db_obj.hour_count * db_obj.per_hour_cost
        db = crud.accounting_balance.update(db=db,
                                            user_id=obj_in.user_id,
                                            add=amount,
                                            commit=False)

        if commit:
            db.commit()
        return db
        # db.refresh(db_obj)
        # return db_obj

    # noinspection PyMethodOverriding
    def update(self, db: Session, obj_in: AccountingHourUpdate, commit: bool = True):
        db_obj = self.get(db, id=obj_in.id)
        if not db_obj:
            raise HTTPException(
                status_code=404,
                detail="The accounting hour with id ({}) does not exist in the system".format(obj_in.id),
            )
        # Update balance
        curr_amount = db_obj.hour_count * db_obj.per_hour_cost
        new_amount = obj_in.hour_count * obj_in.per_hour_cost
        diff_amount = new_amount - curr_amount
        db = crud.accounting_balance.update(db, user_id=db_obj.user_id, add=diff_amount, commit=False)

        # Update accounting hour
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        # db_obj.per_hour_cost = obj_in.per_hour_cost
        # db_obj.hour_count = obj_in.hour_count
        # db_obj.comment = obj_in.comment

        db.add(db_obj)
        if commit:
            db.commit()
        return db
        # db.refresh(db_obj)
        # return db_obj

    # def update_no_commit(self, db: Session,
    #                      db_obj: AccountingHour,
    #                      obj_in: AccountingHourUpdate,
    #                      commit: bool = True):
    #     obj_data = jsonable_encoder(db_obj)
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     db.add(db_obj)
    #     return db

    def get_by_user_id(self, db: Session, user_id: int, min_date: Date, max_date: Date) -> List[AccountingHour]:
        return db.query(self.model).filter(
            self.model.user_id == user_id,
            self.model.day >= min_date,
            self.model.day <= max_date,
            ).options(subqueryload(self.model.project))\
            .all()
    pass


accounting_hour = CRUDAccountingHour(AccountingHour)
