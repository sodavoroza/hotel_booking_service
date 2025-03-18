FROM python:3.12-slim

WORKDIR /app/src

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем зависимости без установки текущего проекта (если не нужен)
RUN poetry install --no-root

# Копируем остальной исходный код
COPY . /app/

# Запускаем сервер
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
