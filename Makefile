install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
test:
	python3 -m pytest -vv --cov=myrepolib tests/*.py
lint:
	pylint --disable=W,R,C,E1101 app.py

format:
	black *.py

all: install lint format