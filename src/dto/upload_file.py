from typing import Any

from fastapi import UploadFile
from pydantic import UUID4, BaseModel


class UploadFileInput(BaseModel):
    file: UploadFile
    template_id: UUID4


class UploadFileOutput(BaseModel):
    file_id: UUID4
    cells: dict[str, Any]
