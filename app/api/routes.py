from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.prices import PriceService
from app.schemas.prices import PriceOut
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/prices", response_model=List[PriceOut])
def get_prices(ticker: str = Query(...), db: Session = Depends(get_db)):
    return PriceService(db).get_all(ticker)

@router.get("/prices/latest", response_model=PriceOut)
def get_latest_price(ticker: str = Query(...), db: Session = Depends(get_db)):
    return PriceService(db).get_latest(ticker)

@router.get("/prices/by-date", response_model=List[PriceOut])
def get_by_date(
    ticker: str = Query(...),
    start: int = Query(...),
    end: int = Query(...),
    db: Session = Depends(get_db)
):
    return PriceService(db).get_by_date(ticker, start, end)
