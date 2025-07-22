import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_attribute_values(
    session: AsyncSession, attribute_id: uuid.UUID
) -> dto.GetAttributeValuesOutput | None:
    # Сначала проверяем, что атрибут существует
    attribute = await postgres.attribute.get_by_id(session, attribute_id)

    if not attribute:
        return None

    # Получаем уникальные значения с количеством использований
    values_with_counts = (
        await postgres.template_attribute.get_unique_values_by_attribute_id(
            session, attribute_id
        )
    )

    # Преобразуем в DTO
    attribute_values = []
    for value, usage_count in values_with_counts:
        attribute_values.append(
            dto.AttributeValue(
                value=value,
                usage_count=usage_count,
            )
        )

    return dto.GetAttributeValuesOutput(
        attribute_id=attribute.id,
        attribute_name=attribute.name,
        values=attribute_values,
        total_count=len(attribute_values),
    )
