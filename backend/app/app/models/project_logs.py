# from typing import TYPE_CHECKING
#
# import datetime
# from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
#
# from app.db.base_class import Base
# from app.models.project_worker import ProjectWorkers
#
# if TYPE_CHECKING:
#     pass
#
#
# class ProjectLogs(Base):
#     __tablename__ = 'project_logs'
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'), index=True)
#     description = Column(String)
#
#     # name = Column(String)
#     # address = Column(String)
#     # created_dt = Column(DateTime, default=datetime.datetime.utcnow)
#     # modified_dt = Column(DateTime, default=datetime.datetime.utcnow)
#     #
#     # workers = relationship('User', secondary=ProjectWorkers.__tablename__, back_populates="project_worker")
