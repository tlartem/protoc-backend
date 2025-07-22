import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_template_attributes(
    session: AsyncSession, template_id: uuid.UUID
) -> dto.GetTemplateAttributesOutput | None:
    # Сначала получаем шаблон
    template = await postgres.template.get(session, template_id)
    if not template:
        return None

    # Получаем атрибуты шаблона
    template_attributes = await postgres.template_attribute.get_by_template_id(
        session, template_id
    )

    # Преобразуем в DTO
    attributes_details = []
    for ta in template_attributes:
        attributes_details.append(
            dto.TemplateAttributeDetail(
                attribute_id=ta.attribute_id,
                attribute_name=ta.attribute.name,
                is_required=ta.attribute.is_required,
                value=ta.value,
                created_at=ta.created_at,
                updated_at=ta.updated_at,
            )
        )

    return dto.GetTemplateAttributesOutput(
        template_id=template.id,
        template_name=template.name,
        attributes=attributes_details,
    )
