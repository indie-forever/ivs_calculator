PYTHON = python3
PIP = pip3
SRC_DIR = src
DOC_DIR = doc
LOGIN = xstudes00_xjanigm00_xformad01_xjindrj00

.PHONY: all pack clean test doc run stddev help install

all: test run

install:
	$(PIP) install --user flet

test:
	$(PYTHON) -m unittest discover $(SRC_DIR)

run:
	$(PYTHON) $(SRC_DIR)/main.py

stddev:
	$(PYTHON) $(SRC_DIR)/stddev

doc:
	doxygen Doxyfile

clean:
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf .pytest_cache
	rm -rf $(DOC_DIR)
	rm -f $(LOGIN).zip

pack: clean
	zip -r $(LOGIN).zip . -x "*.git*" "*.vscode*" "*__pycache__*"

help:
	@echo "all    : Run tests and then the application"
	@echo "install: Install required GUI libraries"
	@echo "run    : Luanch the calculator application"
	@echo "test   : Execute tests"
	@echo "stddev : Run the standard deviation profiling skript"
	@echo "doc    : Generate documentation using Doxygen"
	@echo "clean  : Remove temporary files and archives"
	@echo "pack   : Create a zip archive $(LOGIN).zip for submission"