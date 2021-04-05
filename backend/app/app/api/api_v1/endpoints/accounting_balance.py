from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models
from app.api import deps

router = APIRouter()


@router.get("/recalculate_balance/{user_id}")
def recalculate_balance(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Recalculate balance for the user. Use cases would be when there have been issues with balance calculations (mostly bugs)
    """

    accounting_balance = crud.accounting_balance.recalculate_balance(db, user_id)
    return accounting_balance


@router.get("/{user_id}")
def recalculate_balance(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get user balance
    """

    accounting_balance = crud.accounting_balance.get_by_user_id(db, user_id)
    return accounting_balance
