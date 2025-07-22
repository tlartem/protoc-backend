from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel

from .get_template_attributes import TemplateAttributeDetail


class TemplateWithAttributes(BaseModel):
    id: UUID
    name: str
    description: str | None
    elements: dict[str, Any]
    attributes: list[TemplateAttributeDetail]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


class GetTemplateWithAttributesOutput(BaseModel):
    template: TemplateWithAttributes | None

    class Config:
        from_attributes = True
