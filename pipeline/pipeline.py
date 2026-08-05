import asyncio

from fetch.fetcher import Fetcher
from parse.parser import parse_product

from pipeline.write_queue import write_queue
from db.writer import writer

from reporting.report import Report
from reporting.failed_writer import write_failed


class Pipeline:

    async def run(self):

        report = Report()

        writer_task = asyncio.create_task(
            writer()
        )

        fetcher = Fetcher()

        products = await fetcher.fetch_all()

        report.requested = len(products)

        for product in products:

            if product is None:

                report.failed += 1

                write_failed(
                    {},
                    "Fetch Failed",
                )

                continue

            try:

                validated = parse_product(
                    product
                )

                await write_queue.put(
                    validated
                )

                report.fetched += 1

            except Exception as e:

                report.failed += 1

                write_failed(
                    product,
                    str(e),
                )

        await write_queue.join()

        await write_queue.put(None)

        await writer_task

        report.saved = report.fetched

        report.finish()