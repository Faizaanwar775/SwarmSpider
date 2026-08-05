import asyncio

from config.settings import settings

# Bounded queue for backpressure
write_queue = asyncio.Queue(
    maxsize=settings.BATCH_SIZE * 10
)