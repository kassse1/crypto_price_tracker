from sqlalchemy import Column, Integer, String, Numeric, BigInteger, DateTime
from datetime import datetime
from app.db.session import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    price = Column(Numeric)
    timestamp = Column(BigInteger, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
