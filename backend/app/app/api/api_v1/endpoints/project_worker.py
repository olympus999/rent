from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.accounting_transaction import AccountingTransactionCreate

router = APIRouter()


@router.get("/user/{user_id}/projects")
def get_projects_associated_with_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get project_workers with projects for User
    """

    project_workers = crud.project_worker.projects_associated_with_user(db, user_id)
    return project_workers
