import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def patch_group(
    session: AsyncSession, group_id: uuid.UUID, _input: dto.PatchGroupInput
) -> dto.PatchGroupOutput | None:
    update_data = _input.model_dump(exclude_unset=True)
    group = await postgres.group.update(session, group_id, **update_data)

    if not group:
        return None

    return dto.PatchGroupOutput.model_validate(group)
