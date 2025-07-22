import logging
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.template import Template

logger = logging.getLogger(__name__)


async def get(session: AsyncSession, template_id: uuid.UUID) -> Template | None:
    template = await session.get(Template, template_id)
    if not template:
        return None

    return template


async def get_all(session: AsyncSession) -> list[Template]:
    # Используем более явный запрос без JOIN'ов
    stmt = select(Template).options(
        # Отключаем автоматическую загрузку связанных объектов
    )
    result = await session.execute(stmt)
    templates = result.scalars().unique().all()
    logger.info(f"Database query returned {len(templates)} templates")
    for i, template in enumerate(templates):
        logger.info(f"DB Template {i + 1}: id={template.id}, name={template.name}")
    return templates


async def create(session: AsyncSession, template: Template) -> Template:
    session.add(template)
    await session.commit()
    await session.refresh(template)

    return template


async def update(
    session: AsyncSession, template_id: uuid.UUID, **kwargs
) -> Template | None:
    template = await session.get(Template, template_id)
    if not template:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(template, key, value)

    await session.commit()
    await session.refresh(template)

    return template
