import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_template(
    session: AsyncSession, template_id: uuid.UUID
) -> dto.GetTemplateOutput:
    # Получаем шаблон
    template = await postgres.template.get(session, template_id)
    if not template:
        return dto.GetTemplateOutput(template=None)

    # Получаем все атрибуты системы
    all_attributes = await postgres.attribute.get_all(session)

    # Получаем атрибуты шаблона (те, у которых есть значения)
    template_attributes = await postgres.template_attribute.get_by_template_id(
        session, template_id
    )

    # Создаем словарь для быстрого поиска значений атрибутов
    template_attr_values = {ta.attribute_id: ta for ta in template_attributes}

    # Создаем полный список атрибутов с их значениями или null
    attributes_details = []
    for attr in all_attributes:
        template_attr = template_attr_values.get(attr.id)
        attributes_details.append(
            dto.TemplateAttributeDetail(
                attribute_id=attr.id,
                attribute_name=attr.name,
                is_required=attr.is_required,
                value=template_attr.value if template_attr else None,
            )
        )

    # Создаем объект template с атрибутами
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

    return dto.GetTemplateOutput(template=template_with_attributes)
