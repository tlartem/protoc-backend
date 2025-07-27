import uuid

from pydantic import BaseModel


class DeleteTemplateOutput(BaseModel):
    success: bool
    template_id: uuid.UUID
