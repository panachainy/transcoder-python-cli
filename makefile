f: freeze
freeze:
	pip freeze > requirements.txt

i: install
install:
	pip install -r requirements.txt

r: run
run:
	python3 convert.py
