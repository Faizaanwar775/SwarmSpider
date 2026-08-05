import aiohttp


class FetchClient:
    def __init__(self, timeout: int):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=self.timeout
        )
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def get_json(self, url: str):
        async with self.session.get(url) as response:
            response.raise_for_status()
            return await response.json()