install:
	pip install -r requirements.txt

lint:
	pylint hello.py

test:
	pytest --cov=hello test_hello.py

format:
	black