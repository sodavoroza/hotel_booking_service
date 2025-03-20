![CI](https://github.com/sodavoroza/hotel_booking_service/actions/workflows/ci.yml/badge.svg)

# Hotel Booking Service 🏨

Проект представляет собой REST API для управления бронированием отелей, реализованный на Django и Django REST Framework. 

## Стек технологий

- Python 3.12
- Django 5.1.7
- Django REST Framework 3.15.2
- PostgreSQL 13
- Docker / Docker Compose
- Poetry
- Pytest для тестирования
- Ruff, Black и MyPy для форматирования и статического анализа кода

## 🚀 Быстрый старт

### Локальный запуск (без Docker)

Создайте виртуальное окружение и установите зависимости:

```bash
poetry install
```

Примените миграции:

```bash
poetry run python src/manage.py migrate
```

Запустите сервер разработки:

```bash
poetry run python src/manage.py runserver
```

---

### Запуск с помощью Docker Compose 🐳

Создайте и заполните файл `.env` с необходимыми переменными (см. раздел ниже), затем выполните:

```bash
docker-compose --env-file .env up --build
```

Сервис будет доступен по адресу:
[http://localhost:8000](http://localhost:8000)

## 🔧 Полезные команды Makefile

| Команда            | Описание                                            |
|--------------------|-----------------------------------------------------|
| `make up`          | Запуск Docker Compose (сборка и запуск контейнеров) |
| `make down`        | Остановка всех контейнеров                          |
| `make migrate`     | Выполнение миграций                                 |
| `make test`        | Запуск тестов (pytest) через Docker Compose         |
| `make lint`        | Запустить все линтеры (pre-commit)                  |
| `make format`      | Форматирование кода (ruff, black, isort)            |
| `make mypy`        | Проверка статической типизации                      |
| `make shell`       | Войти в контейнер веб-приложения                    |
| `make logs`        | Посмотреть логи веб-контейнера                      |
| `make ci-check`    | Полная локальная проверка (линтинг, mypy, тесты)    |

## 🧪 Тестирование и линтинг

Запуск тестов:

```bash
make test
```

Линтинг и форматирование кода:

```bash
make lint
make format
```

## 🚦 GitHub Actions (CI/CD)

При каждом пуше запускаются следующие проверки:

- Линтинг и форматирование (ruff, black)
- Проверка типов (mypy)
- Тесты (pytest)

Состояние CI: [![CI](https://github.com/sodavoroza/hotel_booking_service/actions/workflows/ci.yml/badge.svg)](https://github.com/sodavoroza/hotel_booking_service/actions)

## 📚 Документация API (Swagger & Redoc)

Документация доступна только при `DEBUG=True`:

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## 🛠️ Настройки окружения (.env файл)

```env
POSTGRES_DB=hotel
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=your-secret-key
IN_DOCKER=False
```