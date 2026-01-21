from pydantic import BaseModel

class PriceOut(BaseModel):
    ticker: str
    price: float
    timestamp: int

    model_config = {
        "from_attributes": True
    }
