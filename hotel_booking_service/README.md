![CI](https://github.com/sodavoroza/hotel_booking_service/actions/workflows/ci.yml/badge.svg)

## API Endpoints

### Отели
- **GET /api/hotels/** – Получить список отелей.
- **POST /api/hotels/create/** – Создать новый отель.
- **GET /api/hotels/{id}/** – Получить детали отеля.
- **PUT /api/hotels/{id}/update/** – Обновить отель.
- **PATCH /api/hotels/{id}/partial-update/** – Частично обновить отель.
- **DELETE /api/hotels/{id}/delete/** – Удалить отель.

### Номера
- **GET /api/hotels/rooms/** – Получить список номеров.
- **POST /api/hotels/rooms/** – Создать новый номер.
- **DELETE /api/hotels/rooms/{id}/delete/** – Удалить номер и все связанные бронирования.

### Бронирования
- **GET /api/bookings/** – Получить список бронирований.
- **POST /api/bookings/create/** – Создать бронь (требует поля: room, guest_name, check_in, check_out).
- **DELETE /api/bookings/{id}/delete/** – Удалить бронь.
- **GET /api/bookings/list/?room={room_id}** – Получить бронирования для конкретного номера, отсортированные по дате начала.

## Запуск проекта

### Локально
1. Установите зависимости: `poetry install`
2. Примените миграции: `python src/manage.py migrate`
3. Запустите сервер: `python src/manage.py runserver`

### С Docker Compose
1. Запустите: `docker-compose up --build`
# trigger workflow
