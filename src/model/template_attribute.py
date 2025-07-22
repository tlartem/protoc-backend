import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .attribute import Attribute
    from .template import Template


class TemplateAttribute(model.Base):
    __tablename__ = "template_attributes"

    template_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("templates.id"), primary_key=True
    )
    attribute_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("attributes.id"), primary_key=True
    )
    value: Mapped[str | None] = mapped_column(nullable=True)

    template: Mapped["Template"] = relationship(back_populates="template_attributes")
    attribute: Mapped["Attribute"] = relationship(back_populates="template_attributes")
