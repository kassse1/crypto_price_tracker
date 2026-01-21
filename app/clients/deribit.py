from app.core.config import DERIBIT_BASE_URL
import aiohttp
import asyncio
import logging

logger = logging.getLogger(__name__)
TIMEOUT = aiohttp.ClientTimeout(total=5)

class DeribitClient:
    async def get_price(self, ticker: str, retries: int = 3) -> float:
        params = {"index_name": ticker}

        for attempt in range(1, retries + 1):
            try:
                async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
                    async with session.get(DERIBIT_BASE_URL, params=params) as resp:
                        data = await resp.json()

                        if data.get("error"):
                            raise RuntimeError(data["error"])

                        return data["result"]["index_price"]

            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                logger.warning(
                    f"Deribit request failed ({attempt}/{retries}): {e}"
                )
                if attempt == retries:
                    raise
                await asyncio.sleep(1)
