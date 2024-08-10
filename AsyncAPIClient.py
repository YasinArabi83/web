import asyncio
import time

import aiohttp
import json
from aiohttp import ClientSession, TCPConnector, ClientTimeout


class Async_API_Client:
    def __init__(self, api_url: str, headers: dict[str, str], max_connections: int = 100):
        self.api_url = api_url
        self.headers = headers
        self.max_connections = max_connections

    async def fetch(self, session: ClientSession, index):
        print(f"Running fetch coroutine for index {index}")
        timeout = aiohttp.ClientTimeout(total=5)  # Adjust timeout as needed
        try:
            async with session.get(f"{self.api_url}{index}", headers=self.headers, timeout=timeout) as response:
                if response.status == 200:
                    data = await json.loads(await response.read())
                    result = data['data']['ads']
                    return result
                else:
                    return {"error": f"Failed to fetch data (status: {response.status})"}
        except ClientTimeout:
            return {"error": "Request timed out"}
        except Exception as e:  # Catch other potential errors
            return {"error": f"Unexpected error: {e}"}

    async def get_data(self):
        connector = TCPConnector(limit=self.max_connections)
        async with ClientSession(connector=connector) as session:
            tasks = [self.fetch(session, index) for index in range(1, 954)]
            return await asyncio.gather(*tasks, return_exceptions=True)


