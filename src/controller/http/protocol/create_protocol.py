from fastapi import Depends
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, usecase
from src.adapter.postgres import get_session

from . import protocol_router


@protocol_router.post("/")
async def create_protocol(
    input: dto.CreateProtocolInput, session: AsyncSession = Depends(get_session)
) -> Response:
    result = await usecase.create_protocol(session, input)

    return Response(
        content=result.file_content,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": f"attachment; filename=protocol_{result.protocol_id}.xlsx"
        },
    )
