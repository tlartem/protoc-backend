from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Attribute(BaseModel):
    id: UUID
    name: str
    is_required: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetAttributesOutput(BaseModel):
    attributes: list[Attribute]

    class Config:
        from_attributes = True
