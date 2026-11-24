# API Automation Framework (Python + PyTest)

REST API test automation framework built with **Python, PyTest and Requests**, with a **GitHub Actions** CI pipeline.
Tests run against the public [JSONPlaceholder](https://jsonplaceholder.typicode.com) API.

## Features
- Reusable PyTest fixtures (shared session and base URL) in `conftest.py`
- CRUD coverage: GET, POST, PUT, DELETE
- Schema checks, business-rule checks, response-time check and negative scenario (404)
- Parametrized tests and `smoke` / `regression` markers
- HTML test report generated on every run
- GitHub Actions pipeline runs the suite on every push and pull request

## Tech Stack
Python 3.12 · PyTest · Requests · pytest-html · GitHub Actions

## Project Structure
```
api-automation-pytest/
├── .github/workflows/ci.yml
├── tests/
│   ├── test_posts.py
│   └── test_users.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## How to Run
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt

pytest                       # run all tests
pytest -m smoke              # smoke tests only
pytest -m regression         # regression tests only
```
An HTML report is generated as `report.html`.

## Author
Sruthi Adapa · [LinkedIn](https://linkedin.com/in/adapa-sruthi) · [GitHub](https://github.com/Adapasruthi)
