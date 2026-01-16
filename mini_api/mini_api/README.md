# Mini API (FastAPI)

Небольшой REST API на FastAPI.

## Стек
- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

## Запуск
```bash
cd mini_api
unicorn mini_api.app:app --reload

## Документация API

После запуска сервера документация доступна по адресам:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Примеры

### Проверка сервера
**Запрос**
```http
GET /ping

**Ответ:**
```json

{
    "status": "ok",
    "time": "..."
}

### Сложение чисел
```http
POST /sum

**Тело запроса:**
```json

{
    "a": 2,
    "b": 3
}

**Ответ:**
```json

{
    "result": 5
}
