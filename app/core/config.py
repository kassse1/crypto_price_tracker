import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/postgres"
)

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
DERIBIT_BASE_URL = "https://test.deribit.com/api/v2/public/get_index_price"
