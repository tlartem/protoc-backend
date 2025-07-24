from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_standards(session: AsyncSession) -> dto.GetStandardsOutput:
    standards = await postgres.standard.get_all(session)
    return dto.GetStandardsOutput(standards=standards)
