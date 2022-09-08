PYTHON3=/usr/bin/python3
BUILD_DIR=build
DIST_DIR=dist
VIRTUALENV=$(BUILD_DIR)/_virtualenv
VIRTUALENV_BIN=$(VIRTUALENV)/bin
ACTIVATE=$(VIRTUALENV_BIN)/activate

.PHONY: clean test

clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR)

# TODO: linting this way is broken anyway
# lint: $(ACTIVATE)
# 	$(VIRTUALENV_BIN)/python setup.py flake8

test: $(ACTIVATE)
	$(VIRTUALENV_BIN)/python -m unittest discover -v

build-dist: clean $(ACTIVATE) lint test
	$(VIRTUALENV_BIN)/python setup.py sdist bdist_wheel

publish-dist: build-dist
	$(VIRTUALENV_BIN)/pip install twine==1.12.1 && \
		$(VIRTUALENV_BIN)/twine upload dist/*

$(VIRTUALENV) $(ACTIVATE):
	@command -v virtualenv >/dev/null 2>&1 || { echo >&2 "This build requires virtualenv to be installed.  Aborting."; exit 1; }
	@mkdir -p $(BUILD_DIR)
	@if [ -d $(VIRTUALENV) ]; then \
		echo "Existing virtualenv found. Skipping virtualenv creation."; \
	else \
		echo "Creating virtualenv at $(VIRTUALENV)"; \
		virtualenv $(VIRTUALENV) --python=$(PYTHON3); \
	fi
	. $(ACTIVATE) && pip install .
