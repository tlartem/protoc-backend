import uuid

from pydantic import BaseModel

from .set_template_attribute import SetTemplateAttributeInput


class CopyTemplateInput(BaseModel):
    template_id: uuid.UUID
    new_name: str
    new_description: str | None = None
    new_attributes: list[SetTemplateAttributeInput] | None = None


class CopyTemplateOutput(BaseModel):
    new_template_id: uuid.UUID
