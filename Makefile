install:
	uv sync

gendiff:
	uv run gendiff

lint:
	uv run ruff check gendiff

build:
	uv build
	
package-install:
	uv tool install dist/*.whl