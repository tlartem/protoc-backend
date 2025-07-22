from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def create_attribute(
    session: AsyncSession, input: dto.CreateAttributeInput
) -> dto.CreateAttributeOutput:
    # Проверяем, не существует ли уже атрибут с таким именем
    existing_attribute = await postgres.attribute.get_by_name(session, input.name)
    if existing_attribute:
        raise ValueError(f"Атрибут с именем '{input.name}' уже существует")

    attribute = model.Attribute(
        name=input.name,
        is_required=input.is_required,
    )

    created_attribute = await postgres.attribute.create(session, attribute)

    return dto.CreateAttributeOutput(id=created_attribute.id)
