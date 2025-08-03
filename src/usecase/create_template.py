from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def create_template(session: AsyncSession, _input: dto.CreateTemplateInput) -> dto.CreateTemplateOutput:
    # Создаем template
    template = model.Template(
        name=_input.name,
        description=_input.description,
        elements=_input.elements,
        group_id=_input.group_id,
    )
    await postgres.template.create(session, template)

    # Обрабатываем атрибуты, если они переданы
    if _input.attributes is not None:
        for attr_input in _input.attributes:
            # Проверяем, что атрибут существует
            attribute = await postgres.attribute.get_by_id(session, attr_input.attribute_id)
            if not attribute:
                raise ValueError(f"Атрибут с ID {attr_input.attribute_id} не найден")

            # Создаем связь template-attribute
            template_attribute = model.TemplateAttribute(
                template_id=template.id,
                attribute_id=attr_input.attribute_id,
                value=attr_input.value,
            )
            await postgres.template_attribute.create(session, template_attribute)

    return dto.CreateTemplateOutput(id=template.id)
