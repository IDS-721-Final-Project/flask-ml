all: install lint format

install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
lint:
	pylint --disable=W,R,C,E1101 app.py

format:
	black *.py
