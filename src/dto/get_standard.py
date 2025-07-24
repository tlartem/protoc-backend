from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel


class Standard(BaseModel):
    id: UUID
    name: str
    protocol_name: str
    registry_number: str
    range: str
    accuracy: str
    valid_until: date
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetStandardOutput(BaseModel):
    standard: Standard | None
