import uuid

from pydantic import BaseModel


class CreateGroupInput(BaseModel):
    name: str
    order: float = 0
    is_visible: bool = True


class CreateGroupOutput(BaseModel):
    id: uuid.UUID
