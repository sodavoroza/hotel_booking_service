Hotel Booking Service 🏨

[https://github.com/sodavoroza/hotel_booking_service/actions/workflows/ci.yml]

Проект представляет собой REST API для бронирования номеров в отелях, реализованный с помощью Django и Django REST Framework. Он позволяет создавать, редактировать и удалять отели, номера и бронирования, а также отслеживать доступность номеров на указанные даты.

📌 Стек технологий
Python 3.12
Django 5.1.7
Django REST Framework 3.15.2
PostgreSQL
Poetry
Docker и Docker Compose
Pytest
Ruff, Black, Mypy, pre-commit


⚙️ Установка и запуск проекта

🔧 Локальный запуск (без Docker)

1. Клонируйте репозиторий и перейдите в папку проекта
git clone https://github.com/sodavoroza/hotel_booking_service.git
cd hotel_booking_service

2. Создайте и активируйте виртуальное окружение
poetry install

3. Создайте файл .env в корне проекта с таким содержимым:
POSTGRES_DB=hotel
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
IN_DOCKER=False
DJANGO_SECRET_KEY=ваш-секретный-ключ
DJANGO_DEBUG=True

4. Выполните миграции и запустите сервер разработки
poetry run python src/manage.py migrate
poetry run python src/manage.py runserver

Сервер будет доступен по адресу: http://localhost:8000/.



🐳 Запуск через Docker Compose:

1. Создайте файл .env (как описано выше).

2. Запустите приложение через Docker Compose
docker-compose up --build

После запуска приложение доступно на http://localhost:8000/.


📚 Документация API (Swagger и Redoc)

Документация доступна по следующим ссылкам:

Swagger UI: http://localhost:8000/swagger/
Redoc: http://localhost:8000/redoc/


🚀 Доступные API эндпоинты

🏢 Отели
GET /api/hotels/ – список всех отелей
POST /api/hotels/ – создание отеля
GET /api/hotels/{id}/ – детали отеля
PUT /api/hotels/{id}/ – обновление отеля
PATCH /api/hotels/{id}/ – частичное обновление отеля
DELETE /api/hotels/{id}/ – удаление отеля (и всех номеров в нем)

🛏️ Номера
GET /api/rooms/ – список всех номеров
Поддерживается сортировка: ?ordering=price_per_night или ?ordering=-price_per_night
POST /api/rooms/ – создание номера
GET /api/rooms/{id}/ – детали номера
PUT /api/rooms/{id}/ – обновление номера
PATCH /api/rooms/{id}/ – частичное обновление номера
DELETE /api/rooms/{id}/ – удаление номера (и связанных бронирований)

📖 Бронирования
GET /api/bookings/ – список всех бронирований
POST /api/bookings/ – создание бронирования (room, guest_name, check_in, check_out)
GET /api/bookings/{id}/ – детали бронирования
PUT /api/bookings/{id}/ – обновление бронирования
DELETE /api/bookings/{id}/ – удаление бронирования

Дополнительно:

GET /api/bookings/list-by-room/?room_id={room_id} – бронирования по конкретному номеру
DELETE /api/bookings/delete/ – удаление бронирования по booking_id в теле запроса


✅ Проверки качества кода и тестирование

🧹 Линтинг и форматирование:
make lint – проверка кода линтерами (ruff, mypy, black check)
make format – автоформатирование кода (ruff --fix и black)
make up

🧪 Запуск тестов

make test

⚙️ Pre-commit хуки

make pre-commit

🚦 Локальная проверка всего CI-конвейера (линтеры, тесты и pre-commit):

make ci-check


🔄 Continuous Integration (GitHub Actions)

На каждое действие с ветками main и develop запускается автоматическая проверка:

Линтинг и проверка типизации (ruff, black, mypy, pre-commit)
Запуск тестов (pytest)

Настройки находятся в .github/workflows/ci.yml.

Статус сборки:
https://github.com/sodavoroza/hotel_booking_service/actions/workflows/ci.yml