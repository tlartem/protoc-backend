from datetime import date
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class CreateDailyConditionInput(BaseModel):
    laboratory_id: UUID
    measurement_date: date
    conditions: dict[str, Any]


class CreateDailyConditionOutput(BaseModel):
    id: UUID

    class Config:
        from_attributes = True
