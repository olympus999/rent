from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from app.schemas.accounting_transaction import AccountingTransactionCreate

router = APIRouter()


@router.get("/{user_id}")
def recalculate_balance(
    user_id: int,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Recalculate balance for the user. Use cases would be when there have been issues with balance calculations (mostly bugs)
    """

    accounting_balance = crud.accounting_balance.recalculate_balance(db, user_id)
    return accounting_balance
