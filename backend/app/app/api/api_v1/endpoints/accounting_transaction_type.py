from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models
from app.api import deps

router = APIRouter()


@router.get("/")
def get(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get accounting transactions types
    """

    accounting_transactions_types = crud.accounting_transaction_type.get_multi(db)
    return accounting_transactions_types
