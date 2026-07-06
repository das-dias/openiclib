REPO_URL     := https://github.com/IHP-GmbH/TO_Apr2025.git
CLONE_PATH   := pdks/ihp/TO_Apr2025
SPARSE_DIRS  := 160GHz_LNA 40_GHZ_LOW_NOISE_TIA

.PHONY: all init symlinks update clean discover classify pipeline lint test docs help

all: init

## Clone repo with only the specified sparse directories, then create symlinks
init: $(CLONE_PATH)/.git symlinks

$(CLONE_PATH)/.git:
	@echo "[clone] Sparse cloning $(REPO_URL) -> $(CLONE_PATH)"
	git clone --filter=blob:none --no-checkout $(REPO_URL) $(CLONE_PATH)
	cd $(CLONE_PATH) && \
		git sparse-checkout init --cone && \
		git sparse-checkout set $(SPARSE_DIRS) && \
		git checkout

## Create symlinks in pdks/ihp/ pointing into the cloned directories
symlinks:
	@echo "[symlinks] Creating symlinks..."
	@for dir in $(SPARSE_DIRS); do \
		target=pdks/ihp/$$dir; \
		if [ -L $$target ]; then \
			echo "  $$target already exists, skipping."; \
		else \
			ln -s TO_Apr2025/$$dir $$target && \
			echo "  created $$target -> TO_Apr2025/$$dir"; \
		fi \
	done
	git add $(addprefix pdks/ihp/, $(SPARSE_DIRS))
	@echo "[symlinks] Symlinks staged — commit to persist."

## Pull latest changes
update:
	@echo "[update] Pulling latest changes in $(CLONE_PATH)..."
	cd $(CLONE_PATH) && git pull

## Remove the clone and symlinks
clean:
	@echo "[clean] Removing symlinks..."
	@for dir in $(SPARSE_DIRS); do \
		rm -f pdks/ihp/$$dir && echo "  removed pdks/ihp/$$dir"; \
	done
	@echo "[clean] Removing $(CLONE_PATH)..."
	rm -rf $(CLONE_PATH)

## Discover candidate repos from GitHub and GitLab
discover:
	uv run openiclib discover --source all --output candidates.json -v

## Classify candidates into data/designs.json using Claude
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
	@echo "  make init      — sparse clone and create symlinks (default)"
	@echo "  make symlinks  — (re)create symlinks only"
	@echo "  make update    — pull latest changes"
	@echo "  make clean     — remove clone and symlinks"
	@echo "  make discover  — discover IC design repos from GitHub/GitLab"
	@echo "  make classify  — classify candidates into designs.json using Claude"
	@echo "  make pipeline  — full discover → classify → validate pipeline"
	@echo "  make lint      — run ruff linter"
	@echo "  make test      — run pytest"
	@echo "  make docs      — build MkDocs site"
	@echo "  make help      — show this message"
	@echo ""
	@echo "Repo:        $(REPO_URL)"
	@echo "Clone path:  $(CLONE_PATH)"
	@echo "Sparse dirs: $(SPARSE_DIRS)"
	@echo ""