import uuid
from typing import Any

from pydantic import BaseModel


class CreateTemplateInput(BaseModel):
    name: str
    description: str
    elements: dict[str, Any]


class CreateTemplateOutput(BaseModel):
    id: uuid.UUID
