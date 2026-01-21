import asyncio
import logging
from app.tasks.celery_app import celery_app
from app.clients.deribit import DeribitClient
from app.db.session import SessionLocal
from app.services.prices import PriceService

logger = logging.getLogger(__name__)

@celery_app.task(name="app.tasks.fetch_prices.fetch_prices")
def fetch_prices():
    async def run():
        client = DeribitClient()
        db = SessionLocal()
        service = PriceService(db)

        for ticker in ["btc_usd", "eth_usd"]:
            try:
                price = await client.get_price(ticker)
                service.save_price(ticker, price)
            except Exception as e:
                logger.error(f"Failed to fetch {ticker}: {e}")

        db.close()

    asyncio.run(run())
