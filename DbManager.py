from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class AsyncDbManager:
    def __init__(self, db_url):
        self.engine = create_async_engine(db_url, echo=True)
        self.async_session = async_sessionmaker(bind=self.engine, class_=AsyncSession)
