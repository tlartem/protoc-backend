from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def create_standard(
    session: AsyncSession, _input: dto.CreateStandardInput
) -> dto.CreateStandardOutput:
    standard = model.Standard(
        name=_input.name,
        protocol_name=_input.protocol_name,
        registry_number=_input.registry_number,
        range=_input.range,
        accuracy=_input.accuracy,
        valid_until=_input.valid_until,
    )
    await postgres.standard.create(session, standard)
    return dto.CreateStandardOutput(id=standard.id)
