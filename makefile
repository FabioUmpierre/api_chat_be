VENV = .venv
PYTHON = ${VENV}/Scripts/python.exe
all: help
help:
	@echo "Help message"
venv:
	python -m venv ${VENV}
	source ${VENV}/Scripts/activate && pip install -r requirements.txt
clear:
	rm -rf ${VENV}
pyshell:
	${PYTHON}
run:
	${PYTHON} app.py