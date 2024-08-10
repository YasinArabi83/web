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


