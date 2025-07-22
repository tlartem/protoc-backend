from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .template_attribute import TemplateAttribute


class Attribute(Base):
    name: Mapped[str] = mapped_column()
    is_required: Mapped[bool] = mapped_column()

    template_attributes: Mapped[list["TemplateAttribute"]] = relationship()
