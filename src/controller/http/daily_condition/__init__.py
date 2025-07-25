from fastapi import APIRouter

daily_condition_router = APIRouter(
    prefix="/daily-conditions", tags=["daily_conditions"]
)

from . import (
    create_daily_condition,
    delete_daily_condition,
    get_daily_condition,
    get_daily_conditions,
    update_daily_condition,
)
