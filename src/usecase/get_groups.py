from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def get_groups(session: AsyncSession) -> dto.GetGroupsOutput:
    groups = await postgres.group.get_all(session)
    return dto.GetGroupsOutput(groups=groups)
