from model.base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Car(Base):
    __tablename__ = "Car_ads"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    year: Mapped[int] = mapped_column(Integer())
    mileage: Mapped[int] = mapped_column(Integer())
    location: Mapped[str] = mapped_column(String())
    body_color: Mapped[str] = mapped_column(String())
    price: Mapped[int] = mapped_column(Integer())

    def __repr__(self):
        return f"<Car(title='{self.title}', year={self.year}, price={self.price})>"
