import pytest
from aioresponses import aioresponses
from aiohttp import ClientSession
from AsyncAPIClient import AsyncAPIClient  # Replace with the actual module name


@pytest.fixture
def api_client():
    api_url = "https://example.com/api/"
    headers = {"Authorization": "Bearer token"}
    return AsyncAPIClient(api_url, headers)


@pytest.mark.asyncio
async def test_fetch_success(api_client):
    index = 1
    expected_data = {"data": {"ads": ["ad1", "ad2"]}}

    with aioresponses() as m:
        m.get(f"{api_client.api_url}{index}", payload=expected_data)

        async with ClientSession() as session:
            result = await api_client.fetch(session, index)
            assert result == expected_data["data"]["ads"]


@pytest.mark.asyncio
async def test_fetch_failure(api_client):
    index = 1

    with aioresponses() as m:
        m.get(f"{api_client.api_url}{index}", status=404)

        async with ClientSession() as session:
            result = await api_client.fetch(session, index)
            assert result == {"error": "Failed to fetch data (status: 404)"}
