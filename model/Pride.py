
from model.base import Base
from sqlalchemy import  Integer,String
from sqlalchemy.orm import Mapped,mapped_column

class pride (Base):
    __tablename__ = "pride_ads"


    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(150))
    year:Mapped[int]= mapped_column(Integer())
    mileage:Mapped[int]=mapped_column (Integer())
    location : Mapped[str] = mapped_column (String())
    body_color : Mapped[str] = mapped_column(String())
    price : Mapped[int] = mapped_column(Integer())