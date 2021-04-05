from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app import models
from app.api import deps
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
