import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def wait_for_db(max_retries: int = 10, delay: int = 2):
    for attempt in range(1, max_retries + 1):
        try:
            with engine.connect():
                print("✅ Database is ready")
                return
        except OperationalError:
            print(f"⏳ Waiting for database ({attempt}/{max_retries})...")
            time.sleep(delay)
    raise RuntimeError("❌ Database is not available")
