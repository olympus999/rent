from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from app.utils import return_addresses

router = APIRouter()


@router.get("/address_auto_complete/", response_model=Any)
def read_users(
    address: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users.
    """
    if not address:
        raise HTTPException(
            status_code=404,
            detail="No input given",
        )
    return return_addresses(address)
