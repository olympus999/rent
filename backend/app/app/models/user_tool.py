from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class UserTool(Base):
    __tablename__ = 'user_tool'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    tool_id = Column(Integer, ForeignKey('tool.id'), nullable=False)
    details = Column(String)

    __table_args__ = (
        UniqueConstraint('user_id', 'tool_id', name='uix_user_tool_user_id_tool_id'),
    )

    user = relationship('User')
    tool = relationship('Tool')
