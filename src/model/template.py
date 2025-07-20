from typing import TYPE_CHECKING, Any

from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .file import File
    from .sheet import Sheet


class Template(model.Base):
    name: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column(nullable=True)
    elements: Mapped[dict[str, Any]] = mapped_column(JSON)

    file: Mapped["File | None"] = relationship(
        back_populates="template",
        uselist=False,
        lazy="joined",
        cascade="all, delete-orphan",
        single_parent=True,
    )

    sheets: Mapped[list["Sheet"]] = relationship(
        back_populates="template",
        uselist=True,
        lazy="select",
        cascade="all, delete-orphan",
    )
