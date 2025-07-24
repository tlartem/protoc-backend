import uuid
from datetime import date

from pydantic import BaseModel


class PatchStandardInput(BaseModel):
    name: str | None = None
    protocol_name: str | None = None
    registry_number: str | None = None
    range: str | None = None
    accuracy: str | None = None
    valid_until: date | None = None


class PatchStandardOutput(BaseModel):
    id: uuid.UUID
