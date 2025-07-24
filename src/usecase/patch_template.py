import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def patch_template(
    session: AsyncSession, template_id: uuid.UUID, _input: dto.PatchTemplateInput
) -> dto.PatchTemplateOutput | None:
    # Обновляем основные поля template
    update_data = {}
    if _input.name is not None:
        update_data["name"] = _input.name
    if _input.description is not None:
        update_data["description"] = _input.description
    if _input.elements is not None:
        update_data["elements"] = _input.elements

    template = await postgres.template.update(session, template_id, **update_data)
    if not template:
        return None

    # Обрабатываем атрибуты, если они переданы
    if _input.attributes is not None:
        for attr_input in _input.attributes:
            # Проверяем, что атрибут существует
            attribute = await postgres.attribute.get_by_id(
                session, attr_input.attribute_id
            )
            if not attribute:
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
                await postgres.template_attribute.create(
                    session, new_template_attribute
                )

    return dto.PatchTemplateOutput(id=template.id)
