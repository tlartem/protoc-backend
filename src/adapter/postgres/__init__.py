__all__ = [
    "get_session",
    "create_tables",
    "db_dispose",
    "template",
    "file",
    "sheet",
    "attribute",
    "template_attribute",
    "standard",
    "laboratory",
    "condition_type",
    "daily_condition",
    "group",
]

from shared.db_helper import DatabaseHelper
from src.config import settings

from . import (
    attribute,
    condition_type,
    daily_condition,
    file,
    group,
    laboratory,
    sheet,
    standard,
    template,
    template_attribute,
)

db_helper = DatabaseHelper(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

get_session = db_helper.get_session_dependency()
db_dispose = db_helper.dispose
create_tables = db_helper.create_tables
