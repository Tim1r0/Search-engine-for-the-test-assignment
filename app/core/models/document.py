from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Document(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    rubrics: Mapped[list[str]] = mapped_column()
    text: Mapped[str] = mapped_column()
    created_date: Mapped[datetime] = mapped_column()