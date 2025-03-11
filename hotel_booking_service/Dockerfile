FROM python:3.12-slim

# Установим рабочую директорию
WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock /app/

# Установим Poetry
RUN pip install poetry

# Копируем README.md в контейнер
COPY README.md /app/

# Устанавливаем зависимости проекта
RUN poetry install

# Запускаем контейнер
CMD ["python", "manage.py", "runserver"]
