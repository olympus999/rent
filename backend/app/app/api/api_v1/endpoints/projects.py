from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Project])
def get_all(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_client_or_superuser),
) -> Any:
    """
    Retrieve projects
    """
    if not crud.user.is_superuser(current_user):
        projects = crud.project.get_multi(db)
    else:
        projects = crud.project.get_multi_for_client(db,  user_id=current_user.id)
    return projects


@router.post('/', response_model=schemas.ProjectCreate)
def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_client_or_superuser),
) -> Any:
    """
    Create project
    """
    crud.project.create(db, obj_in=project_in, user_id=current_user.id)
    return True
