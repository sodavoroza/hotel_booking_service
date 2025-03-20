up:
	docker-compose --env-file .env up -d --build

down:
	docker-compose --env-file .env down

migrate:
	docker-compose --env-file .env exec web poetry run python src/manage.py migrate

test:
	docker-compose --env-file .env exec web bash -c "PYTHONPATH=src poetry run pytest src/ --disable-warnings"

shell:
	docker-compose --env-file .env exec web bash

logs:
	docker-compose --env-file .env logs -f web

lint:
	poetry run pre-commit run --all-files

format:
	poetry run ruff check . --fix
	poetry run black .
	poetry run isort .

mypy:
	poetry run mypy src

ci-check: lint mypy test

