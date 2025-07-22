from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_attributes(session: AsyncSession) -> dto.GetAttributesOutput:
    attributes = await postgres.attribute.get_all(session)
    return dto.GetAttributesOutput(attributes=attributes)
