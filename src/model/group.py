from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .template import Template


class Group(model.Base):
    name: Mapped[str]
    order: Mapped[float] = mapped_column(default=0)
    is_visible: Mapped[bool] = mapped_column(default=True)

    templates: Mapped[list["Template"]] = relationship(
        back_populates="group",
        uselist=True,
        lazy="select",
    )
