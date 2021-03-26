from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.accounting_transaction import AccountingTransactionCreate

router = APIRouter()


@router.get("/user/{user_id}")
def get_accounting_transactions_by_user_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get accounting transactions for user
    """

    accounting_transactions = crud.accounting_transaction.get_by_user_id(db, user_id)
    return accounting_transactions


@router.post('/')
def set_accounting_transaction(
    accounting_transaction_in: AccountingTransactionCreate,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Set accounting transaction
    """

    accounting_transaction = crud.accounting_transaction.create(db, obj_in=accounting_transaction_in)
    return accounting_transaction
