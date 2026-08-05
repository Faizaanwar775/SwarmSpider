import asyncio
from typing import List

from config.settings import settings
from fetch.client import FetchClient
from fetch.retry import fetch_with_retry


class Fetcher:
    def __init__(self):
        self.semaphore = asyncio.Semaphore(
            settings.FETCH_CONCURRENCY
        )

    async def _fetch_one(
        self,
        client: FetchClient,
        url: str,
    ):
        async with self.semaphore:

            return await fetch_with_retry(
                client.session,
                url,
            )

    async def fetch_all(self) -> List[dict]:

        async with FetchClient(
            settings.REQUEST_TIMEOUT
        ) as client:

            tasks = []

            for page in range(
                1,
                settings.TOTAL_PAGES + 1,
            ):

                url = (
                    f"{settings.BASE_URL}/product/{page}"
                )

                tasks.append(
                    asyncio.create_task(
                        self._fetch_one(
                            client,
                            url,
                        )
                    )
                )

            results = await asyncio.gather(
                *tasks,
                return_exceptions=False,
            )

            return results