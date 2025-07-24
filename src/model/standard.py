from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from src import model


class Standard(model.Base):
    name: Mapped[str] = mapped_column()
    protocol_name: Mapped[str] = mapped_column()
    registry_number: Mapped[str] = mapped_column()
    range: Mapped[str] = mapped_column()
    accuracy: Mapped[str] = mapped_column()
    valid_until: Mapped[date] = mapped_column()
