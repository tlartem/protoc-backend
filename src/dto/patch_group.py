import uuid
from datetime import datetime

from pydantic import BaseModel


class PatchGroupInput(BaseModel):
    name: str | None = None
    order: float | None = None
    is_visible: bool | None = None


class PatchGroupOutput(BaseModel):
    id: uuid.UUID
    name: str
    order: float
    is_visible: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True
