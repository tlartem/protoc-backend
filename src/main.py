from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.adapter.postgres import create_tables, db_dispose
from src.controller.http import (
    attribute,
    daily_condition,
    file,
    laboratory,
    protocol,
    sheet,
    standard,
    template,
    upload_file,
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # Создаем таблицы при запуске
    await create_tables()
    yield
    await db_dispose()


app: FastAPI = FastAPI(lifespan=lifespan, docs_url="/", version="0.0.1")

# Routers
app.include_router(upload_file.upload_file_router)
app.include_router(template.template_router)
app.include_router(file.file_router)
app.include_router(sheet.sheet_router)
app.include_router(protocol.protocol_router)
app.include_router(attribute.attribute_router)
app.include_router(standard.standard_router)
app.include_router(laboratory.laboratory_router)
app.include_router(daily_condition.daily_condition_router)
