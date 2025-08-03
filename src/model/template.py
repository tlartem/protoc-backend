import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

from .group import Group

if TYPE_CHECKING:
    from .file import File
    from .sheet import Sheet
    from .template_attribute import TemplateAttribute


class Template(model.Base):
    name: Mapped[str] = mapped_column()
    description: Mapped[str | None]
    elements: Mapped[dict[str, Any]] = mapped_column(JSON)
    order: Mapped[float] = mapped_column(default=0.0)

    group_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("groups.id", ondelete="SET NULL"))
    group: Mapped[Group | None] = relationship(back_populates="templates")

    files: Mapped[list["File"]] = relationship(
        back_populates="template",
        uselist=True,
        lazy="select",
        cascade="all, delete-orphan",
    )

    sheets: Mapped[list["Sheet"]] = relationship(
        back_populates="template",
        uselist=True,
        lazy="select",
        cascade="all, delete-orphan",
    )

    template_attributes: Mapped[list["TemplateAttribute"]] = relationship(cascade="all, delete-orphan")
