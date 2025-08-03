from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Group(BaseModel):
    id: UUID
    name: str
    order: float
    is_visible: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetGroupOutput(BaseModel):
    group: Group | None
