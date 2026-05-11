SUBMODULE_URL  := https://github.com/IHP-GmbH/TO_Apr2025.git
SUBMODULE_PATH := pdks/ihp/TO_Apr2025
SPARSE_DIRS    := 160GHz_LNA 40_GHZ_LOW_NOISE_TIA

.PHONY: all init update clean help

all: init

## Set up the submodule and configure sparse-checkout
init: $(SUBMODULE_PATH)/.git
	@echo "[sparse-checkout] Configuring sparse-checkout..."
	cd $(SUBMODULE_PATH) && \
		git sparse-checkout init --cone && \
		git sparse-checkout set $(SPARSE_DIRS)
	@echo "[sparse-checkout] Done. Active directories:"
	cd $(SUBMODULE_PATH) && git sparse-checkout list

## Add the submodule if it doesn't exist yet
$(SUBMODULE_PATH)/.git:
	@echo "[submodule] Adding $(SUBMODULE_URL) -> $(SUBMODULE_PATH)"
	git submodule add --force $(SUBMODULE_URL) $(SUBMODULE_PATH)
	git submodule update --init $(SUBMODULE_PATH)

## Pull latest changes in the submodule
update:
	@echo "[submodule] Updating $(SUBMODULE_PATH)..."
	git submodule update --remote $(SUBMODULE_PATH)

## Remove the submodule entirely
clean:
	@echo "[submodule] Removing $(SUBMODULE_PATH)..."
	git submodule deinit -f $(SUBMODULE_PATH)
	git rm -f $(SUBMODULE_PATH)
	rm -rf .git/modules/$(SUBMODULE_PATH)
	@echo "[submodule] Done. Remember to commit the changes."

help:
	@echo ""
	@echo "Targets:"
	@echo "  make init    — add submodule and configure sparse-checkout (default)"
	@echo "  make update  — pull latest changes from upstream submodule"
	@echo "  make clean   — remove the submodule entirely"
	@echo "  make help    — show this message"
	@echo ""
	@echo "Sparse dirs: $(SPARSE_DIRS)"
	@echo "Submodule:   $(SUBMODULE_PATH)"
	@echo ""