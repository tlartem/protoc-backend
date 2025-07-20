from typing import Any
from uuid import UUID

from pydantic import BaseModel


class PatchTemplateInput(BaseModel):
    name: str | None = None
    description: str | None = None
    elements: dict[str, Any] | None = None


class PatchTemplateOutput(BaseModel):
    id: UUID
