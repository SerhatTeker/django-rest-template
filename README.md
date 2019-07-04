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

### It Worked!

Go to: http://localhost:8000/


## Testing our API:

### 1. Superuser/Admin creation
```bash
# migrate db
$ python manage.py migrate

# create superuser
$ python manage.py createsuperuser --email admin@example.com --username admin
# then set password `password123`

```
### 2. Test

```bash
# using tools like curl:
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/

# or httpie:
$ http -a admin:password123 http://127.0.0.1:8000/users/

# or go to URL:
$ firefox http://127.0.0.1:8000/users/
```


------

## TODOs

+ [x] add logging.ini config
+ [x] add editorconfig
