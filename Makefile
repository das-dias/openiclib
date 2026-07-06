.PHONY: discover classify pipeline lint test docs help

## Discover candidate repos from GitHub and GitLab
discover:
	uv run openiclib discover --source all --output candidates.json -v

## Classify candidates into data/designs.json
classify:
	uv run openiclib classify --input candidates.json --output data/designs.json -v

## Full pipeline: discover → classify → validate
pipeline: discover classify
	uv run openiclib db validate

## Run linter
lint:
	uv run ruff check .

## Run tests
test:
	uv run pytest

## Build docs
docs:
	uv run mkdocs build --strict

help:
	@echo ""
	@echo "Targets:"
	@echo "  make discover  — discover IC design repos from GitHub/GitLab"
	@echo "  make classify  — classify candidates into designs.json"
	@echo "  make pipeline  — full discover → classify → validate pipeline"
	@echo "  make lint      — run ruff linter"
	@echo "  make test      — run pytest"
	@echo "  make docs      — build MkDocs site"
	@echo "  make help      — show this message"
	@echo ""
