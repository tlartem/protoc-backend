from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_laboratories(session: AsyncSession) -> dto.GetLaboratoriesOutput:
    laboratories = await postgres.laboratory.get_all(session)
    return dto.GetLaboratoriesOutput(laboratories=laboratories)
