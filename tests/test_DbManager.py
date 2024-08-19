import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base
from DbManager import DbManager


@pytest.fixture(scope='module')
def engine():
    return create_engine('sqlite:///:memory:')


@pytest.fixture(scope='module')
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='function')
def session(engine, tables):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope='function')
def db_manager(session):
    return DbManager(db_path='sqlite:///:memory:', session=session)


def test_save_to_db(db_manager):
    ads = [
        {"title": "Car 1", "year": 2020, "mileage": 10000, "location": "Location 1", "body_color": "Red",
         "price": 20000},
        {"title": "Car 2", "year": 2019, "mileage": 20000, "location": "Location 2", "body_color": "Blue",
         "price": 15000}
    ]
    db_manager.save_to_db(ads)
    all_ads = db_manager.get_all()
    assert len(all_ads) == 2
    assert all_ads[0].title == "Car 1"
    assert all_ads[1].title == "Car 2"


def test_get_all(db_manager):
    ads = [
        {"title": "Car 3", "year": 2021, "mileage": 5000, "location": "Location 3", "body_color": "Green",
         "price": 25000}
    ]
    db_manager.save_to_db(ads)
    all_ads = db_manager.get_all()
    assert len(all_ads) == 1
    assert all_ads[0].title == "Car 3"
