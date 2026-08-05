# SwarmSpider

## Features

- Async aiohttp scraping
- Concurrent fetching
- Retry with exponential backoff
- Pydantic validation
- Async SQLAlchemy
- SQLite database
- Connection pooling
- Write throttling
- Backpressure using asyncio.Queue
- Idempotent writes
- Failed page logging
- Summary reporting

## Run

Start server:

python mock_server/server.py

Run scraper:

python main.py