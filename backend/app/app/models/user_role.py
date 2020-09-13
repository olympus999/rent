from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class UserRole(Base):
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True)
    name = Column(String,  unique=True)
