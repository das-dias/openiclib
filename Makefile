SUBMODULE_URL         := https://github.com/IHP-GmbH/TO_Apr2025.git
SUBMODULE_PATH        := pdks/ihp/TO_Apr2025
SPARSE_CHECKOUT_FILE  := $(SUBMODULE_PATH)/.sparse-checkout

.PHONY: all init update clean help

all: init

## Set up the submodule and apply sparse-checkout from committed config file
init: $(SUBMODULE_PATH)/.git $(SPARSE_CHECKOUT_FILE)
	@echo "[sparse-checkout] Applying $(SPARSE_CHECKOUT_FILE)..."
	cd $(SUBMODULE_PATH) && \
		git sparse-checkout init --cone && \
		git sparse-checkout set $(cat ../.sparse-checkout)
	@echo "[sparse-checkout] Done. Active directories:"
	cd $(SUBMODULE_PATH) && git sparse-checkout list

## Add the submodule if it doesn't exist yet
$(SUBMODULE_PATH)/.git:
	@echo "[submodule] Adding $(SUBMODULE_URL) -> $(SUBMODULE_PATH)"
	git submodule add --force $(SUBMODULE_URL) $(SUBMODULE_PATH)
	git submodule update --init $(SUBMODULE_PATH)

## Generate the .sparse-checkout config file and commit it
$(SPARSE_CHECKOUT_FILE):
	@echo "[sparse-checkout] Creating $(SPARSE_CHECKOUT_FILE)..."
	@printf '160GHz_LNA\n40_GHZ_LOW_NOISE_TIA\n' > $(SPARSE_CHECKOUT_FILE)
	git add $(SPARSE_CHECKOUT_FILE)
	@echo "[sparse-checkout] $(SPARSE_CHECKOUT_FILE) created and staged — commit it to persist."

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
	@echo "  make init    — add submodule and apply sparse-checkout from config (default)"
	@echo "  make update  — pull latest changes from upstream submodule"
	@echo "  make clean   — remove the submodule entirely"
	@echo "  make help    — show this message"
	@echo ""
	@echo "Sparse config: $(SPARSE_CHECKOUT_FILE)"
	@echo "Submodule:     $(SUBMODULE_PATH)"
	@echo ""