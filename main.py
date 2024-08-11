import asyncio
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from AsyncAPIClient import AsyncAPIClient
from DataProcessor import DataProcessor
from DbManager import DbManager
from model.base import Base

headers = {
    "User-Agent": "Your User Agent",
    "Accept": "application/json",
    "Referer": "https://bama.ir/",
    "Cookie": "Your Cookie Here"
}

curl = AsyncAPIClient('https://bama.ir/cad/api/search?pageIndex=', headers, max_connections=100)


async def main():
    start_time = time.time()
    data = await curl.get_data()
    end_time = time.time()
    successful_data = [result for result in data if "error" not in result]

    print(len(successful_data))
    print(end_time - start_time)
    return successful_data


if __name__ == '__main__':
    engine = create_engine('sqlite:///Ads.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    db_manager = DbManager("sqlite:///Ads.db", session)
    while True:
        print(" =========================== \n"
              "Menu \n \n"
              "1. Update db \n"
              "2. Get all \n"
              "3. Get cars between pricest\n"
              "4. Exit\n\n"
              "===========================")
        choice = input("What`s your choice: ")

        if choice == "1":
            raw_data = asyncio.run(main())
            data_processor = DataProcessor(raw_data)
            car_ads = data_processor.data_processor()
            db_manager.save_to_db(car_ads)

        elif choice == "2":
            all_ads = db_manager.get_all()
            for ad in all_ads:
                print(ad)
        elif choice == "3":
            start_price = int(input("What`s your starting price: "))
            end_price = int(input("What`s your ending price: "))
            ads = db_manager.get_cars_between_prices(start_price, end_price)
            for ad in ads:
                print(ad)
        elif choice == "4":
            break
        else:
            print("Invalid selection. Please select again.\n")