from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from src import model

if TYPE_CHECKING:
    from .file import File
    from .sheet import Sheet


class Template(model.Base):
    name: Mapped[str]
    description: Mapped[str | None]


    file: Mapped["File"] = relationship(
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