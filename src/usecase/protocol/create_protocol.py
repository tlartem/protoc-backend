import uuid

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto
from src.adapter import excel, postgres


async def create_protocol(
    session: AsyncSession, input: dto.CreateProtocolInput
) -> dto.CreateProtocolOutput:
    file = await postgres.file.get(session, input.file_id)
    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
        )

    # Заполняем ячейки и получаем модифицированный файл
    modified_file_content = excel.fill_cells(input.cells_to_update, file.content)

    return dto.CreateProtocolOutput(
        protocol_id=uuid.uuid4(), file_content=modified_file_content
    )
