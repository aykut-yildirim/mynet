VENV := venv

all:
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip3 install -r requirements.txt
	$(VENV)/bin/activate: requirements.txt

venv: 
	$(VENV)/bin/activate

run:
	./$(VENV)/bin/python3 main.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	tm -rf __pycache__

make_requirements:
	pip freeze > requirements.txt

.PHONY: 
	all venv run clean