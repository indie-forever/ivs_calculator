PYTHON = python3
SRC_DIR = src

.PHONY: all test clean run


all: test

test:
	$(PYTHON) -m unittest discover $(SRC_DIR)

run:
	$(PYTHON) $(SRC_DIR)/main.py

clean:
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf .pytest_cache