from typing import Optional, List
from datetime import datetime, date
from decimal import Decimal

from pydantic import BaseModel, EmailStr, DecimalMaxPlacesError
# from . import project_worker


# Shared properties
class AccountingHourBase(BaseModel):
    user_id: int = None
    project_id: int = None
    day: date = None
    hour_count: Decimal = 0
    per_hour_cost: Decimal = 0
    comment: Optional[str] = None
    modified_dt: datetime = None
    created_dt: datetime = None

    class Config:
        orm_mode = True


class AccountingHourCreate(BaseModel):
    user_id: int = None
    project_id: int = None
    day: date = None
    hour_count: Decimal = 0
    per_hour_cost: Decimal = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True


class AccountingHourUpdate(BaseModel):
    id: int = None
    hour_count: Optional[Decimal] = 0
    per_hour_cost: Optional[Decimal] = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True


class AccountingHourCreateOrUpdate(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    project_id: Optional[int] = None
    day: Optional[date] = None

    hour_count: Decimal = 0
    per_hour_cost: Decimal = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True


class AccountingHour(AccountingHourBase):
    id: int = None
    pass
