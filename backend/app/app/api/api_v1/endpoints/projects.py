from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.models.project_worker import ProjectWorker
from app.crud.utils import update_or_create_project

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/admin", response_model=List[schemas.ProjectWithProjectWorker])
def get_all(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_client_or_superuser),
) -> Any:
    """
    Retrieve projects
    """
    projects = crud.project.get_many_projects_with_workers(db)
    return projects


@router.get("/admin/removed", response_model=List[schemas.ProjectWithProjectWorker])
def get_all(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_client_or_superuser),
) -> Any:
    """
    Retrieve projects
    """
    projects = crud.project.get_many_projects_with_workers(db, return_removed=True)
    return projects


@router.put("/admin/{project_id}", response_model_exclude_unset=True)
def update_project(
    project_in: schemas.ProjectAdminCreateUpdate,
    # project_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update project
    """
    return update_or_create_project(db, project_in=project_in)


@router.post("/admin/", response_model_exclude_unset=True)
def create_project(
    project_in: schemas.ProjectAdminCreateUpdate,
    # user_id: int,
    # project_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update project
    """
    return update_or_create_project(db, project_in=project_in)


@router.delete('/admin/{project_id}', response_model_exclude_unset=True)
def delete_project(
    project_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete project
    """

    project = crud.project.delete(db, project_id)

    return project


# @router.get("/client", response_model=List[schemas.ProjectWithProjectWorker])
# def get_all(
#     db: Session = Depends(deps.get_db),
#     current_user: models.User = Depends(deps.get_current_active_client_or_superuser),
# ) -> Any:
#     """
#     Retrieve projects
#     """
#     projects = crud.project.get_many_projects_with_workers(db)
#     return projects

