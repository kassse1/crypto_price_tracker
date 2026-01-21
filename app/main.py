from fastapi import FastAPI
from app.api.routes import router
from app.db.session import Base, engine, wait_for_db

app = FastAPI(title="Deribit Prices API")

@app.on_event("startup")
def on_startup():
    wait_for_db()
    Base.metadata.create_all(bind=engine)

app.include_router(router)
