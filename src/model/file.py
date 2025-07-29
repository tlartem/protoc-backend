import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy import JSON, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .template import Template


class File(model.Base):
    name: Mapped[str] = mapped_column()
    content: Mapped[bytes] = mapped_column(LargeBinary)
    cells: Mapped[dict[str, Any]] = mapped_column(JSON())
    template_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("templates.id"), nullable=True
    )

    template: Mapped["Template"] = relationship(
        back_populates="files",
        uselist=False,
        lazy="joined",
    )
