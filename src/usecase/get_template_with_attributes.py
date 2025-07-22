import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_template_with_attributes(
    session: AsyncSession, template_id: uuid.UUID
) -> dto.GetTemplateWithAttributesOutput:
    # Получаем шаблон
    template = await postgres.template.get(session, template_id)
    if not template:
        return dto.GetTemplateWithAttributesOutput(template=None)

    # Получаем атрибуты шаблона
    template_attributes = await postgres.template_attribute.get_by_template_id(
        session, template_id
    )

    # Преобразуем атрибуты в DTO
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

    # Создаем шаблон с атрибутами
    template_with_attributes = dto.TemplateWithAttributes(
        id=template.id,
        name=template.name,
        description=template.description,
        elements=template.elements,
        attributes=attributes_details,
        created_at=template.created_at,
        updated_at=template.updated_at,
        deleted_at=template.deleted_at,
    )

    return dto.GetTemplateWithAttributesOutput(template=template_with_attributes)
