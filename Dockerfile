FROM python:3.12-slim

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем зависимости без установки текущего проекта (если не нужен)
RUN poetry install --no-root

# Копируем остальной исходный код
COPY . .

# Запускаем сервер
CMD ["poetry", "run", "python", "src/hotel_booking_service/manage.py", "runserver", "0.0.0.0:8000"]
