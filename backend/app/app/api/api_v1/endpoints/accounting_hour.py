from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from datetime import date

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from app.schemas.accounting_hour import AccountingHourCreateOrUpdate, AccountingHour

router = APIRouter()


@router.get("/user/{user_id}/{min_date}/{max_date}")
def get_accounting_hours_by_user_id(
        user_id: int,
        min_date: date,
        max_date: date,
        db: Session = Depends(deps.get_db),
        # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get accounting hours for user
    """

    accounting_hours = crud.accounting_hour.get_by_user_id(db, user_id, min_date, max_date)
    return accounting_hours


@router.post('/')
def set_accounting_hour(
    accounting_hour_in: List[AccountingHourCreateOrUpdate],
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> List[AccountingHour]:
    """
    Set accounting hour
    """

    accounting_hour = crud.accounting_hour.create_or_update_multi(db, _in=accounting_hour_in)
    return accounting_hour
