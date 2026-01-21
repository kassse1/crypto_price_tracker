Данный проект представляет собой backend-сервис для сбора и хранения index price криптовалют с биржи Deribit.

Сервис периодически получает текущие цены btc_usd и eth_usd через публичный Deribit API, сохраняет их в базе данных PostgreSQL и предоставляет HTTP API для получения последней цены и исторических данных за выбранный временной диапазон.

---

##  Features

- Periodic price fetching (every minute)
- Persistent price history storage
- REST API (GET only)
- Fault-tolerant external API handling (retry & timeout)
- Unit tests for business logic
- Dockerized environment

---

##  Tech Stack

- **Python 3.11**
- **FastAPI**
- **PostgreSQL**
- **Celery + Redis**
- **aiohttp**
- **SQLAlchemy**
- **Docker / Docker Compose**
- **pytest**

---

##  Architecture

Проект разделён на слои:

- **API layer** — FastAPI endpoints
- **Service layer** — бизнес-логика работы с ценами
- **Client layer** — HTTP-клиент Deribit
- **DB layer** — модели и сессии БД
- **Background workers** — Celery tasks для периодического сбора данных

Такое разделение упрощает тестирование и поддержку кода.

---

##  Installation & Run

### 1️⃣ Запуск проекта

```bash
docker-compose up --build
Будут запущены следующие сервисы:

API (FastAPI)

Celery worker + Celery beat

PostgreSQL

Redis

 How to verify the application works
1️⃣ Проверка периодического сбора данных
Подождите 1–2 минуты после запуска.

В логах Celery должно появиться:

arduino
Копировать код
Task app.tasks.fetch_prices.fetch_prices succeeded
2️⃣ Проверка базы данных (опционально)
bash
Копировать код
docker exec -it crypto_price_tracker-db-1 psql -U postgres
sql
Копировать код
SELECT * FROM prices;
Вы должны увидеть записи для btc_usd и eth_usd.

3️⃣ Проверка API
Swagger UI:

bash
Копировать код
http://localhost:8000/docs
Получить все данные по валюте
bash
Копировать код
curl "http://localhost:8000/prices?ticker=btc_usd"
Получить последнюю цену
bash
Копировать код
curl "http://localhost:8000/prices/latest?ticker=btc_usd"
Получить цены за период
bash
Копировать код
curl "http://localhost:8000/prices/by-date?ticker=btc_usd&start=1700000000&end=1800000000"
 Run tests
Тесты запускаются внутри Docker-контейнера:

bash
Копировать код
docker exec -it crypto_price_tracker-api-1 python -m pytest
 Design Decisions
Используются public endpoints Deribit API, так как получение index price не требует аутентификации.

Данные сохраняются как временной ряд (append-only), без обновления существующих записей.

Последняя цена определяется как последняя вставленная запись (по id), что надёжнее, чем сортировка по timestamp.

Внешний API может быть нестабилен, поэтому реализованы retry и timeout.

Unit-тесты покрывают сервисный слой, где сосредоточена бизнес-логика.
