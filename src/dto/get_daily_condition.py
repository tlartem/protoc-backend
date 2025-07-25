from __future__ import annotations

from datetime import date, datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class DailyCondition(BaseModel):
    id: UUID
    laboratory_id: UUID
    measurement_date: date
    conditions: dict[str, Any]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetDailyConditionOutput(BaseModel):
    daily_condition: DailyCondition | None

    class Config:
        from_attributes = True
