from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Company(Base):
    __tablename__ = "company"

    # Vi kan skippa mapped_column om vi inte ska lägga till constraints
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    postal_code: Mapped[str]
    email: Mapped[str]
    description: Mapped[str] = mapped_column(Text)  # onödig mapped_column
    analytics_module: Mapped[bool]

    def __repr__(self):
        return f"<Company={self.name}>"
