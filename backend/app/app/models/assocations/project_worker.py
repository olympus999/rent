import datetime
from sqlalchemy import Integer, ForeignKey, Table, Column, DateTime
from app.db.base_class import Base

ProjectWorkers = Table('project_worker', Base.metadata,
                       Column('project_id', Integer, ForeignKey('project.id')),
                       Column('user_id', Integer, ForeignKey('user.id'), unique=True),
                       Column('created_dt', DateTime, default=datetime.datetime.utcnow)
                       )
