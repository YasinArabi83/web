from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from model.Car import Car
from model.base import Base


class AsyncDbManager:
    def __init__(self, db_url):
        self.engine = create_async_engine(db_url, echo=True)
        self.async_session = async_sessionmaker(bind=self.engine, class_=AsyncSession)

    async def create_table(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def save_to_db(self, car_ad: dict):
        async with self.async_session() as session:
            async with session.begin():
                new_record = Car(**car_ad)
                session.add(new_record)
