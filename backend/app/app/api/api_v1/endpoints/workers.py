from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Worker])
def read_workers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_client_or_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_workers(db, skip=skip, limit=limit)
    return users
