from typing import TYPE_CHECKING

from sqlalchemy import JSONB, LargeBinary
from sqlalchemy.orm import Mapped, relationship

from src import model

if TYPE_CHECKING:
    from .template import Template


class File(model.Base):
    name: Mapped[str]
    content: Mapped[bytes] = LargeBinary
    cells: Mapped[JSONB]

    template: Mapped["Template"] = relationship(
        back_populates="file",
        uselist=False,
        lazy="joined",
        cascade="all, delete-orphan",
        single_parent=True,
    )
