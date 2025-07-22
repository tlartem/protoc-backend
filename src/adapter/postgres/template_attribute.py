import logging
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.model.template_attribute import TemplateAttribute

logger = logging.getLogger(__name__)


async def get_by_template_id(
    session: AsyncSession, template_id: uuid.UUID
) -> list[TemplateAttribute]:
    """Получает все атрибуты для конкретного шаблона с загруженными связанными данными"""
    stmt = (
        select(TemplateAttribute)
        .options(joinedload(TemplateAttribute.attribute))
        .where(TemplateAttribute.template_id == template_id)
    )
    result = await session.execute(stmt)
    template_attributes = result.scalars().unique().all()
    logger.info(
        f"Found {len(template_attributes)} attributes for template {template_id}"
    )
    return template_attributes


async def create(
    session: AsyncSession, template_attribute: TemplateAttribute
) -> TemplateAttribute:
    """Создает новую связь атрибута с шаблоном"""
    session.add(template_attribute)
    await session.commit()
    await session.refresh(template_attribute)
    return template_attribute


async def update_value(
    session: AsyncSession,
    template_id: uuid.UUID,
    attribute_id: uuid.UUID,
    value: str | None,
) -> TemplateAttribute | None:
    """Обновляет значение атрибута для шаблона"""
    stmt = select(TemplateAttribute).where(
        TemplateAttribute.template_id == template_id,
        TemplateAttribute.attribute_id == attribute_id,
    )
    result = await session.execute(stmt)
    template_attribute = result.scalar_one_or_none()

    if not template_attribute:
        return None

    template_attribute.value = value
    await session.commit()
    await session.refresh(template_attribute)
    return template_attribute


async def get_unique_values_by_attribute_id(
    session: AsyncSession, attribute_id: uuid.UUID
) -> list[tuple[str, int]]:
    """Получает уникальные значения атрибута с количеством использований"""
    from sqlalchemy import func

    stmt = (
        select(
            TemplateAttribute.value,
            func.count(TemplateAttribute.template_id).label("usage_count"),
        )
        .where(
            TemplateAttribute.attribute_id == attribute_id,
            TemplateAttribute.value.is_not(None),  # Исключаем NULL значения
        )
        .group_by(TemplateAttribute.value)
        .order_by(
            func.count(TemplateAttribute.template_id).desc()
        )  # Сортировка по популярности
    )

    result = await session.execute(stmt)
    values_with_counts = result.all()
    logger.info(
        f"Found {len(values_with_counts)} unique values for attribute {attribute_id}"
    )

    return [(row.value, row.usage_count) for row in values_with_counts]
