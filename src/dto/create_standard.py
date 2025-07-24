import uuid
from datetime import date

from pydantic import BaseModel


class CreateStandardInput(BaseModel):
    name: str
    protocol_name: str
    registry_number: str
    range: str
    accuracy: str
    valid_until: date


class CreateStandardOutput(BaseModel):
    id: uuid.UUID
