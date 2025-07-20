from typing import Any
from uuid import UUID

from pydantic import BaseModel


class PatchSheetInput(BaseModel):
    name: str | None = None
    cells: dict[str, Any] | None = None


class PatchSheetOutput(BaseModel):
    id: UUID
