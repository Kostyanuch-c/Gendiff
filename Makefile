install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

gendif:
	poetry run gendiff

gendiff_gui:
	poetry run gendiff_gui

check: selfcheck test lint

selfcheck:
	poetry check

build:check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

.PHONY: install test lint selfcheck check build