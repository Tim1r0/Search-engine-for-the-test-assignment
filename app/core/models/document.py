from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ARRAY, String
from .base import Base


class Document(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rubrics: Mapped[list[str]] = mapped_column(ARRAY(String))
    text: Mapped[str] = mapped_column()
    created_date: Mapped[datetime] = mapped_column()