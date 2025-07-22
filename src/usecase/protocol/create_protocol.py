import uuid

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import postgres
from src.adapter.excel import fill_cells


async def create_protocol(
    session: AsyncSession, input: dto.CreateProtocolInput
) -> dto.CreateProtocolOutput:
    file = await postgres.file.get(session, input.file_id)
    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )

    # Заполняем ячейки (это мок, результат не сохраняем)
    fill_cells(input.cells_to_update, file.content)
    print(input.cells_to_update)

    return dto.CreateProtocolOutput(protocol_id=uuid.uuid4())
