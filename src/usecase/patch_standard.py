import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres


async def patch_standard(
    session: AsyncSession, standard_id: uuid.UUID, _input: dto.PatchStandardInput
) -> dto.PatchStandardOutput | None:
    update_data = {}
    if _input.name is not None:
        update_data["name"] = _input.name
    if _input.protocol_name is not None:
        update_data["protocol_name"] = _input.protocol_name
    if _input.registry_number is not None:
        update_data["registry_number"] = _input.registry_number
    if _input.range is not None:
        update_data["range"] = _input.range
    if _input.accuracy is not None:
        update_data["accuracy"] = _input.accuracy
    if _input.valid_until is not None:
        update_data["valid_until"] = _input.valid_until

    standard = await postgres.standard.update(session, standard_id, **update_data)
    if not standard:
        return None

    return dto.PatchStandardOutput(id=standard.id)
