from fastapi import Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src import usecase
from src.adapter.postgres import get_session

from . import daily_condition_router


@daily_condition_router.delete("/{daily_condition_id}")
async def delete_daily_condition(
    daily_condition_id: UUID4,
    session: AsyncSession = Depends(get_session),
) -> dict[str, str]:
    success = await usecase.delete_daily_condition(session, daily_condition_id)
    if not success:
        raise HTTPException(status_code=404, detail="Daily condition not found")
    return {"message": "Daily condition deleted successfully"}
