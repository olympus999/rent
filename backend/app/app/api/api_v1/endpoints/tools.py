from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/")
def get_tools(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get tools
    """
    tools = crud.tool.get_multi(db)
    return tools


@router.post("/")
def create_tool(
    tool_in: schemas.ToolCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create tool
    """
    tool_in.name = tool_in.name.lower()
    tool = crud.tool.get_by_name(db, name=tool_in.name)
    if tool:
        raise HTTPException(
            status_code=400,
            detail="The tool with this name already exists.",
        )
    tool = crud.tool.create(db, obj_in=tool_in)
    return tool


@router.put("/{tool_id}")
def update_tool(
    tool_in: schemas.ToolUpdate,
    tool_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update tools
    """
    tool_in.name = tool_in.name.lower()
    tool = crud.tool.get_by_name(db, name=tool_in.name)
    if tool:
        raise HTTPException(
            status_code=400,
            detail="The tool with this name already exists.",
        )
    tool = crud.tool.get(db, id=tool_id)
    tool = crud.tool.update(db, db_obj=tool, obj_in=tool_in)
    return tool


@router.delete("/{tool_id}")
def delete_tool(
    tool_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get clients only
    """
    print('tool_id', tool_id)
    tool = crud.tool.remove(db, id=tool_id)
    return tool
