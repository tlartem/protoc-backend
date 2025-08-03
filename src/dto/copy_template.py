import uuid

from pydantic import BaseModel

from .set_template_attribute import SetTemplateAttributeInput


class CopyTemplateInput(BaseModel):
    template_id: uuid.UUID
    new_name: str
    new_description: str | None = None
    new_attributes: list[SetTemplateAttributeInput] | None = None
    group_id: uuid.UUID | None = None
    copy_first_sheet_empty: bool = False


class CopyTemplateOutput(BaseModel):
    new_template_id: uuid.UUID
