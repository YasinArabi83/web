import asyncio

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from model.Car import Car
from model.base import Base


class DbManager:
    def __init__(self, db_path: str,session):
        self.session = session

    def save_to_db(self, ads):
        cars = [Car(**ad) for ad in ads]
        self.session.add_all(cars)
        self.session.commit()
        print('Ads saved')

    def get_all(self):
        x = self.session.query(Car).all()
        return x