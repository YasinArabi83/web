from aiohttp import ClientSession
import asyncio

class Async_API_Client:
    def __init__(self, api_url:str ,headers:dict[str,str]) :
        self.api_url = api_url
        self.headers = headers

    async def fetch(self,  session: ClientSession, index):
        print("running fetch coroutine")
        async with session.get(f"{self.api_url}{index}", headers=self.headers) as response:
            if response.status == 200:

                data = await response.json()
                result = data['data']['ads']
                return result
            else:
                return {"error": "Failed to fetch data"}
    
    async def get_data(self):
        async with ClientSession() as session:
            tasks = [self.fetch(session, index) for index in range(1, 11)]
            return await asyncio.gather(*tasks,return_exceptions=True)
