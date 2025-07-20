import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.template import Template


async def get(session: AsyncSession, template_id: uuid.UUID) -> Template | None:
    template = await session.get(Template, template_id)
    if not template:
        return None

    return template


async def get_all(session: AsyncSession) -> list[Template]:
    templates = await session.execute(select(Template))
    return list(templates.scalars().all())


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
