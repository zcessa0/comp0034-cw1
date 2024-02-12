# COMP0034 2023-24 Coursework 1

This is a Flask REST API for interacting with free school meal data in England.

## Setup

First create a virtual environment before you can run this project.
### Install Dependencies 
Install required packages:
```
pip install -r requirements.txt
```
### Run the App 
To run the Flask app in development:
```
flask --app coursework1 run --debug
```
### Test
To run the test suite:
```
python -m pytest
```



The project structure follows
the ['Tests as part of the application code'](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#tests-as-part-of-application-code)
structure. This is to make it easier for you to submit a single folder for the coursework.

Do not delete, move or rename the following files and folders:

- `LICENSE`
- `README.md`
- `.gitignore`
- `pyproject.toml`
- `requirements.txt`
- `src/__init__.py`
- `src/coursework1` and the files within it: `__init__.py`,`data_prep.py`
- `src/coursework2` and the files within it: `__init__.py`,`employee.py`
- `src/coursework2/tests` and the files within it: `__init__.py`,`test_code.py`, `test_employee.py`
