PYTHON = python3
TEST_DIR = test_math.py

.PHONY: all test clean run help


all: help

test:
	python3 src/test_math.py

run:
	$(PYTHON) src/main.py

clean:
	rm -rf src/__pycache__
	rm -rf __pycache__
	rm -rf .pytest_cache