from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Integer


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
    )

    price: Mapped[float] = mapped_column(
        Float,
    )

    category: Mapped[str] = mapped_column(
        String(100),
    )

    url: Mapped[str] = mapped_column(
        String(300),
        unique=True,
    )