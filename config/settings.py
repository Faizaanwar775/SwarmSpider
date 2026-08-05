from dataclasses import dataclass


@dataclass
class Settings:
    BASE_URL = "http://127.0.0.1:8000"

    TOTAL_PAGES = 120

    FETCH_CONCURRENCY = 20

    WRITE_CONCURRENCY = 5

    DB_POOL_SIZE = 5

    MAX_RETRIES = 3

    REQUEST_TIMEOUT = 5

    BATCH_SIZE = 10


settings = Settings()
