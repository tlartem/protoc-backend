import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_laboratory(
    session: AsyncSession, laboratory_id: uuid.UUID
) -> dto.GetLaboratoryOutput:
    laboratory = await postgres.laboratory.get(session, laboratory_id)
    return dto.GetLaboratoryOutput(laboratory=laboratory)
