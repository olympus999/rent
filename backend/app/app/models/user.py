from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.assocations.project_worker import ProjectWorkers

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    role = Column(String, ForeignKey('user_role.name'))
    available = Column(Boolean, default=True, server_default='1', nullable=False)
    items = relationship("Item", back_populates="owner")

    project = relationship('Project')

    project_worker = relationship('Project', secondary=ProjectWorkers, back_populates="workers")
