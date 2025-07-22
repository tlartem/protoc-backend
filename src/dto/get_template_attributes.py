from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class TemplateAttributeDetail(BaseModel):
    attribute_id: UUID
    attribute_name: str
    is_required: bool
    value: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class GetTemplateAttributesOutput(BaseModel):
    template_id: UUID
    template_name: str
    attributes: list[TemplateAttributeDetail]

    class Config:
        from_attributes = True
