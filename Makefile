build:
		docker compose -f local.yml up --build -d --remove-orphans

up:
		docker compose -f local.yml up -d 

down: 
		docker compose -f local.yml down

logs:

		docker compose -f local.yml logs

api-logs:

		docker compose -f local.yml api

makemigrations:

		docker compose -f local.yml run --rm api manage.py makemigrations

migrate:

		docker compose -f local.yml run --rm api python manage.py migrate 

collectstatic:

		docker compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:

		docker compose -f local.yml run --rm api python manage.py createsuperuser 

down-v:

		docker compose -f local.yml down -v 

