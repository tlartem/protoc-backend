__all__ = ("template", "file", "sheet", "attribute", "template_attribute")

from shared.db_helper import DatabaseHelper
from src.config import settings

from . import attribute, file, sheet, template, template_attribute

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
