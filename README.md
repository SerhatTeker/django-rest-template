# Quick Start

## Requirements

- Python 3.6 or higher
- Django 2.0.12


## Basic installation

```bash
# install virtual environment
$ virtualenv -p python3 .venv
# activate virtual environment
$ source .venv/bin/activate
# install requirements
$ pip install -r requirements.txt
# migrate database
$ ./manage.py migrate
```

## Running

```bash
$ ./manage.py runserver
# or
make run
```

## It Worked!

Go to: http://localhost:8000/


------

## TODOs

+ [ ] add logging.ini config
