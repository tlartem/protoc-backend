from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ConditionType(BaseModel):
    id: UUID
    name: str
    unit: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class Laboratory(BaseModel):
    id: UUID
    name: str
    condition_types: list[ConditionType]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetLaboratoryOutput(BaseModel):
    laboratory: Laboratory | None

    class Config:
        from_attributes = True
