import uuid
from datetime import date
from typing import TYPE_CHECKING, Any

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import model

if TYPE_CHECKING:
    from .laboratory import Laboratory


class DailyCondition(model.Base):
    __tablename__ = "daily_conditions"

    laboratory_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("laboratorys.id"))
    measurement_date: Mapped[date] = mapped_column()
    conditions: Mapped[dict[str, Any]] = mapped_column(JSON)

    laboratory: Mapped["Laboratory"] = relationship(back_populates="daily_conditions")
