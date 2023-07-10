init:
	code .
	poetry config --local virtualenvs.create true
	poetry config --local virtualenvs.in-project true
	poetry env use 3.10
	poetry install
	poetry update
	git init
	echo ".venv/" >> .gitignore
	echo "logs/" >> .gitignore
	poetry export -f requirements.txt --output requirements.txt
	git add .
	poetry run pre-commit run --all-files
	git commit -am "Initial commit after initializing the project."
	poetry shell

test:
	pytest .

coverage:
	pytest --cov=coolors_preview tests/
