up:
	docker-compose --env-file .env up -d --build

down:
	docker-compose --env-file .env down

migrate:
	docker-compose --env-file .env exec web poetry run python src/manage.py migrate

test:
	docker-compose --env-file .env exec web bash -c "PYTHONPATH=src poetry run pytest src/"

shell:
	docker-compose --env-file .env exec web bash

logs:
	docker-compose --env-file .env logs -f web
lint:
	docker-compose --env-file .env exec web poetry run ruff check src

format:
	docker-compose --env-file .env exec web poetry run black src && \
	docker-compose --env-file .env exec web poetry run isort src

mypy:
	docker-compose --env-file .env exec web poetry run mypy src
