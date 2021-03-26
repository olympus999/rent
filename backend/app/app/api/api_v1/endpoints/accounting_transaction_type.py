from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.accounting_transaction import AccountingTransactionCreate

router = APIRouter()


@router.get("/")
def get(
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get accounting transactions types
    """

    accounting_transactions_types = crud.accounting_transaction_type.get_multi(db)
    return accounting_transactions_types
