import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def set_template_attributes(
    session: AsyncSession, template_id: uuid.UUID, input: dto.SetTemplateAttributesInput
) -> list[dto.SetTemplateAttributeOutput]:
    # Проверяем, что шаблон существует
    template = await postgres.template.get(session, template_id)
    if not template:
        raise ValueError(f"Шаблон с ID {template_id} не найден")

    results = []

    for attr_input in input.attributes:
        # Проверяем, что атрибут существует
        attribute = await postgres.attribute.get_all(session)
        attribute_exists = any(attr.id == attr_input.attribute_id for attr in attribute)
        if not attribute_exists:
            raise ValueError(f"Атрибут с ID {attr_input.attribute_id} не найден")

        # Пытаемся обновить существующую связь
        template_attribute = await postgres.template_attribute.update_value(
            session, template_id, attr_input.attribute_id, attr_input.value
        )

        # Если связи нет, создаем новую
        if not template_attribute:
            new_template_attribute = model.TemplateAttribute(
                template_id=template_id,
                attribute_id=attr_input.attribute_id,
                value=attr_input.value,
            )
            template_attribute = await postgres.template_attribute.create(
                session, new_template_attribute
            )

        results.append(
            dto.SetTemplateAttributeOutput(
                template_id=template_id,
                attribute_id=attr_input.attribute_id,
                value=template_attribute.value,
            )
        )

    return results
