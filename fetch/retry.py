import asyncio
import logging
import aiohttp

from config.settings import settings

logger = logging.getLogger(__name__)


async def fetch_with_retry(session, url: str):
    """
    Fetch a URL with retry and exponential backoff.
    """

    delay = 1

    for attempt in range(1, settings.MAX_RETRIES + 1):

        try:

            async with session.get(url) as response:

                response.raise_for_status()

                logger.info(
                    f"SUCCESS | {url} | Status {response.status}"
                )

                return await response.json()

        except (
            aiohttp.ClientError,
            asyncio.TimeoutError,
        ) as e:

            logger.warning(
                f"Attempt {attempt}/{settings.MAX_RETRIES} failed for {url}: {e}"
            )

            if attempt == settings.MAX_RETRIES:

                logger.error(
                    f"FAILED | {url}"
                )

                return None

            await asyncio.sleep(delay)

            delay *= 2