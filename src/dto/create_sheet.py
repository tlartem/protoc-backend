from typing import Any
from uuid import UUID

from pydantic import BaseModel


class CreateSheetInput(BaseModel):
    name: str
    cells: dict[str, Any]
    template_id: UUID


class CreateSheetOutput(BaseModel):
    id: UUID
