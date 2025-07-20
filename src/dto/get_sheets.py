from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class Sheet(BaseModel):
    id: UUID
    name: str
    cells: dict[str, Any]
    template_id: UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetSheetsOutput(BaseModel):
    sheets: list[Sheet]
