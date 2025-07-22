from uuid import UUID

from pydantic import BaseModel


class AttributeValue(BaseModel):
    """Значение атрибута с дополнительной информацией"""

    value: str
    usage_count: int  # Количество шаблонов, которые используют это значение

    class Config:
        from_attributes = True


class GetAttributeValuesOutput(BaseModel):
    """Список уникальных значений атрибута"""

    attribute_id: UUID
    attribute_name: str
    values: list[AttributeValue]
    total_count: int  # Общее количество уникальных значений

    class Config:
        from_attributes = True
