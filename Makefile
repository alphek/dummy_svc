# TODO I need get rid of sudo commands and use proper user

help:
	@echo "Docker Compose Help"
	@echo "-----------------------"
	@echo ""
	@echo "Run tests to ensure current state is good:"
	@echo "    make test"
	@echo ""
	@echo "If tests pass, add fixture data and start up the api:"
	@echo "    make begin"
	@echo ""
	@echo "Really, really start over:"
	@echo "    make clean"
	@echo ""
	@echo "See contents of Makefile for more targets."

build:
	@sudo docker-compose build

start:
	@sudo docker-compose up -d

stop:
	@sudo docker-compose stop

status:
	@sudo docker ps

restart: stop start

clean: stop
	@sudo docker-compose rm --force

test:
	@sudo docker-compose run --rm dummy_svc pytest

showmigrations:
	@sudo docker-compose run --rm dummy_svc python ./manage.py showmigrations

makemigrations:
	@sudo docker-compose run --rm dummy_svc python ./manage.py makemigrations

migrate:
	@sudo docker-compose run --rm dummy_svc python ./manage.py migrate

