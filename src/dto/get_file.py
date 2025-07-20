from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class File(BaseModel):
    id: UUID
    name: str
    cells: dict[str, Any]
    template_id: UUID | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetFileOutput(BaseModel):
    file: File | None
