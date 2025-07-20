import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.sheet import Sheet


async def get(session: AsyncSession, sheet_id: uuid.UUID) -> Sheet | None:
    sheet = await session.get(Sheet, sheet_id)
    if not sheet:
        return None

    return sheet


async def get_all(session: AsyncSession) -> list[Sheet]:
    sheets = await session.execute(select(Sheet))
    return list(sheets.scalars().all())


async def get_by_template(session: AsyncSession, template_id: uuid.UUID) -> list[Sheet]:
    sheets = await session.execute(
        select(Sheet).where(Sheet.template_id == template_id)
    )
    return list(sheets.scalars().all())


async def create(session: AsyncSession, sheet: Sheet) -> Sheet:
    session.add(sheet)
    await session.commit()
    await session.refresh(sheet)

    return sheet


async def update(session: AsyncSession, sheet_id: uuid.UUID, **kwargs) -> Sheet | None:
    sheet = await session.get(Sheet, sheet_id)
    if not sheet:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(sheet, key, value)

    await session.commit()
    await session.refresh(sheet)

    return sheet
