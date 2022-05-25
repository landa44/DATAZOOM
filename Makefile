build:
	docker build --force-rm $(options) -t datazoom_beta:latest .

build-prod: 
	${MAKE} build options="--target production" 

compose-start:
	docker compose up --remove-orphans $(options)

compose-stop:
	docker compose down --remove-orphans $(options)

compose-manage-py:
	docker compose run --rm $(options) website python manage.py $(cmd)

compose-black:
	docker compose run --rm $(options) website black $(cmd)