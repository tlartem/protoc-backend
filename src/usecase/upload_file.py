import uuid

from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import excel, postgres


async def upload_file(session: AsyncSession, file: UploadFile, template_id: uuid.UUID) -> dto.UploadFileOutput:
    file_content = await file.read()
    cells_data = excel.read_cells(file_content)
    
    output = await postgres.file.create(session, model.File(
        name=file.filename,
        content=file_content, 
        cells=cells_data,
        template_id=template_id,
    ))

    return dto.UploadFileOutput(
        file_id=output.id,
        cells=output.cells
    )

