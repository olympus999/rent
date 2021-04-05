from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from app.schemas.user_feedback import UserFeedbackCreate, UserFeedbackUpdate

router = APIRouter()


@router.post('/', response_model=schemas.UserFeedbackCreate)
def create_user_feedback(
        user_feedback_in: schemas.UserFeedbackCreate,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Add feedback for user per project
    """
    user_feedback_in_copy = user_feedback_in.copy()
    user_feedback_in_copy.feedback_given_user_id = current_user.id

    user_feedback = crud.user_feedback.create(db, obj_in=user_feedback_in_copy)

    return user_feedback

