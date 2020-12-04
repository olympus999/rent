from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Project])
def get_all(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve available user roles
    """
    projects = crud.project.get_all(db)
    return projects


@router.post('/', response_model=schemas.ProjectCreateIncludeWorkers)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    project_in: schemas.ProjectCreateIncludeWorkers,
    # current_user: models.User = Depends(deps.get_current_active_client_or_superuser),
) -> Any:
    """
    Create project
    """
    print(project_in)
    project = crud.project.create(db, project_in)
    return project
