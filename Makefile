.ONESHELL:
SHELL = /bin/bash

use-env:
	@source .venv/bin/activate

create-env:
	python3 -m venv .venv

install-requirements: use-env
	@pip install -r requirements.txt

run: use-env
	flask --app odontolab run --debug

gen-requirements: use-env
	pip freeze > requirements.txt