import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.file import File


async def get(session: AsyncSession, file_id: uuid.UUID) -> File | None:
    file = await session.get(File, file_id)
    if not file:
        return None

    return file


async def get_all(session: AsyncSession) -> list[File]:
    files = await session.execute(select(File))
    return list(files.scalars().all())


async def get_by_template(session: AsyncSession, template_id: uuid.UUID) -> list[File]:
    files = await session.execute(select(File).where(File.template_id == template_id))
    return list(files.scalars().all())


async def create(session: AsyncSession, file: File) -> File:
    session.add(file)
    await session.commit()
    await session.refresh(file)

    return file
