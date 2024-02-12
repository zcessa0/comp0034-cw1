# COMP0034 2023-24 Coursework 1

This is a Flask REST API for interacting with free school meal data in England.

- Link to GitHub Repository: https://github.com/zcessa0/comp0034-cw1

I made the mistake of not working in the repository in the ucl-comp0035 organisation. I do have one but I temporarily switched to another repository to continue my work, however, I forgot to move back to the organization repository once the issue was resolved. Since moving the repository would involve losing commit history, I've decided to continue my work in the current repository. I apologise for any confusion this may have caused. 

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

The project structure follows the 'Tests as part of the application code' structure. This is to make it easier for you to submit a single folder for the coursework.

Do not delete, move or rename the following files and folders:
- `LICENSE`
- `README.md`
- `.gitignore`
- `pyproject.toml`
- `requirements.txt`
- `src/coursework1` and the files within it : `__init__.py`, `model.py`, `routes.py` and `schema.py`
- `src/coursework1/data` and the files within it: `dataset.xlsx`, `dataset_prepared.csv` and `dataset_prepared.xlxs`
- `src/tests` and the files within it: `conftest.py` and `test_routes.py`
- `src/comp0034-coursework1.md` and `src/testing_ss.png` used to explain testing procedure.
