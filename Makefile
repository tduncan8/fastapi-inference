.PHONY: install run clean

install:
	pip install -r requirements.txt

run:
	uvicorn app:app --reload

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete