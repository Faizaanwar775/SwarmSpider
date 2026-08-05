import asyncio
import logging

from pipeline.write_queue import write_queue
from db.crud import save_product
from config.settings import settings

logger = logging.getLogger(__name__)

write_semaphore = asyncio.Semaphore(
    settings.WRITE_CONCURRENCY
)


async def writer():

    while True:

        product = await write_queue.get()

        if product is None:

            write_queue.task_done()

            logger.info("Writer stopped.")

            break

        try:

            async with write_semaphore:

                saved = await save_product(product)

                if saved:
                    logger.info(
                        f"Saved Product {product.id}"
                    )
                else:
                    logger.info(
                        f"Duplicate skipped {product.id}"
                    )

        except Exception as e:

            logger.exception(e)

        finally:

            write_queue.task_done()