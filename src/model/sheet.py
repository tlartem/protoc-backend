import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .template import Template


class Sheet(model.Base):
    name: Mapped[str]
    cells: Mapped[dict[str, Any]] = mapped_column(JSON)
    template_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("templates.id"))

    template: Mapped["Template"] = relationship(back_populates="sheets")
