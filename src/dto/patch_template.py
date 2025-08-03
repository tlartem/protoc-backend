from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel

from .set_template_attribute import SetTemplateAttributeInput


class PatchTemplateInput(BaseModel):
    name: str | None = None
    description: str | None = None
    elements: dict[str, Any] | None = None
    attributes: list[SetTemplateAttributeInput] | None = None
    group_id: UUID | Literal["ungroup"] | None = None
    order: float | None = None


class PatchTemplateOutput(BaseModel):
    id: UUID
