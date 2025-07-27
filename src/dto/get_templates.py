from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel

from .get_template import TemplateWithAttributes


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


class GetTemplatesOutput(BaseModel):
    templates: list[TemplateWithAttributes]

    class Config:
        from_attributes = True
