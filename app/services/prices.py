from sqlalchemy.orm import Session
from app.db.models import Price
import time

class PriceService:
    def __init__(self, db: Session):
        self.db = db

    def save_price(self, ticker: str, price: float):
        record = Price(
            ticker=ticker,
            price=price,
            timestamp=int(time.time())
        )
        self.db.add(record)
        self.db.commit()

    def get_all(self, ticker: str):
        return self.db.query(Price).filter(Price.ticker == ticker).all()

    def get_latest(self, ticker: str):
        return (
            self.db.query(Price)
            .filter(Price.ticker == ticker)
            .order_by(Price.id.desc())
            .first()
        )

    def get_by_date(self, ticker: str, start: int, end: int):
        return (
            self.db.query(Price)
            .filter(
                Price.ticker == ticker,
                Price.timestamp >= start,
                Price.timestamp <= end
            )
            .all()
        )
