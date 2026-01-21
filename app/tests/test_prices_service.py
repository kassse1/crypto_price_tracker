from app.services.prices import PriceService


def test_save_price(db_session):
    service = PriceService(db_session)

    service.save_price("btc_usd", 100.0)

    result = service.get_all("btc_usd")
    assert len(result) == 1
    assert result[0].ticker == "btc_usd"
    assert float(result[0].price) == 100.0

def test_get_latest_price(db_session):
    service = PriceService(db_session)

    service.save_price("btc_usd", 100.0)
    service.save_price("btc_usd", 200.0)

    latest = service.get_latest("btc_usd")

    assert latest is not None
    assert float(latest.price) == 200.0
