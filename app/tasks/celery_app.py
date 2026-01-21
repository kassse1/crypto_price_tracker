from celery import Celery
from app.core.config import REDIS_URL

celery_app = Celery(
    "app",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["app.tasks.fetch_prices"]  # 🔥 ВАЖНО
)

celery_app.conf.beat_schedule = {
    "fetch-prices-every-minute": {
        "task": "app.tasks.fetch_prices.fetch_prices",
        "schedule": 60.0
    }
}
