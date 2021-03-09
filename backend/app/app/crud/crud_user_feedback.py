from app.crud.base import CRUDBase
from app.models.user_feedback import UserFeedback
from app.schemas.user_feedback import UserFeedbackCreate, UserFeedbackUpdate


class CRUDUserFeedback(CRUDBase[UserFeedback, UserFeedbackCreate, UserFeedbackUpdate]):
    pass


user_feedback = CRUDUserFeedback(UserFeedback)
