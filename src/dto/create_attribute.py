import uuid

from pydantic import BaseModel


class CreateAttributeInput(BaseModel):
    name: str
    is_required: bool


class CreateAttributeOutput(BaseModel):
    id: uuid.UUID
