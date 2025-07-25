from __future__ import annotations

from datetime import date
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class UpdateDailyConditionInput(BaseModel):
    laboratory_id: UUID | None = None
    measurement_date: date | None = None
    conditions: dict[str, Any] | None = None


class UpdateDailyConditionOutput(BaseModel):
    id: UUID

    class Config:
        from_attributes = True
