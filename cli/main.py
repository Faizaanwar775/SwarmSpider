import asyncio

from db.init_db import init_db

from pipeline.pipeline import Pipeline


async def main():

    await init_db()

    pipeline = Pipeline()

    await pipeline.run()


if __name__ == "__main__":

    asyncio.run(main())