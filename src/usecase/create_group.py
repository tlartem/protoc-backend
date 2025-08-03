from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def create_group(session: AsyncSession, _input: dto.CreateGroupInput) -> dto.CreateGroupOutput:
    group = model.Group(
        name=_input.name,
        order=_input.order,
        is_visible=_input.is_visible,
    )
    await postgres.group.create(session, group)
    return dto.CreateGroupOutput(id=group.id)
