import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, DateTime, func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Tool(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    created_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    modified_dt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.current_timestamp())
