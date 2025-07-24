import uuid
from typing import Any

from pydantic import BaseModel

from .set_template_attribute import SetTemplateAttributeInput


class CreateTemplateInput(BaseModel):
    name: str
    description: str
    elements: dict[str, Any]
    attributes: list[SetTemplateAttributeInput] | None = None


class CreateTemplateOutput(BaseModel):
    id: uuid.UUID
