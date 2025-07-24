from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class TemplateAttributeDetail(BaseModel):
    attribute_id: UUID
    attribute_name: str
    is_required: bool
    value: str | None

    class Config:
        from_attributes = True


class Template(BaseModel):
    id: UUID
    name: str
    description: str | None
    elements: dict[str, Any]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    class Config:
        from_attributes = True


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


class GetTemplateOutput(BaseModel):
    template: TemplateWithAttributes | None
