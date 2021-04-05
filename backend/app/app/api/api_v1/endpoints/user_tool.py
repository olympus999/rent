from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/user/{user_id}", response_model=List[schemas.user_tool.UserToolWithToolDetails])
def get_user_tools(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get all tools assigned to user
    """
    user_tools = crud.user_tool.get_by_user_id(db, user_id)
    return user_tools


@router.post("/")
def add_tool_to_user(
    user_tool_in: schemas.UserToolCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Add tool to user
    """
    user_tool = crud.user_tool.create(db, obj_in=user_tool_in)
    return user_tool


@router.put("/{user_tool_id}")
def update_user_tool(
    user_tool_in: schemas.UserToolUpdate,
    user_tool_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update user_tool description
    """
    user_tool = crud.user_tool.get(db, user_tool_id)
    if user_tool.details != user_tool_in.details:
        user_tool.details = user_tool_in.details
        db.commit()
        db.refresh(user_tool)
    return user_tool


@router.delete("/{user_tool_id}")
def remove_user_tool(
    user_tool_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Remove user_tool
    """
    crud.user_tool.remove(db, id=user_tool_id)
    return True
