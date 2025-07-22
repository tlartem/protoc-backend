import uuid

from pydantic import BaseModel


class SetTemplateAttributeInput(BaseModel):
    attribute_id: uuid.UUID
    value: str | None


class SetTemplateAttributesInput(BaseModel):
    """Для установки множественных атрибутов за один раз"""

    attributes: list[SetTemplateAttributeInput]


class SetTemplateAttributeOutput(BaseModel):
    template_id: uuid.UUID
    attribute_id: uuid.UUID
    value: str | None
