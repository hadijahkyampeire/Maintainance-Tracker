[![Build Status](https://travis-ci.org/hadijahkyampeire/Maintainance-Tracker.svg?branch=master)](https://travis-ci.org/hadijahkyampeire/Maintainance-Tracker)
[![Coverage Status](https://coveralls.io/repos/github/hadijahkyampeire/Maintainance-Tracker/badge.svg?branch=master)](https://coveralls.io/github/hadijahkyampeire/Maintainance-Tracker?branch=master)
# Maintainance-Tracker
Maintenance Tracker App is a product that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

#### To access the UI templates online visit [Maintainance App](https://hadijahkyampeire.github.io/Maintainance-Tracker/)

## Requirements(Building Blocks)
- `Python3` - A programming language that lets us work more quickly (The universe loves speed!).
- `Flask` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
- `Virtualenv` - A tool to create isolated virtual environment
- `PostgreSQL` – Postgres database offers many advantages over others.
- `Psycopg2` – A Python adapter for Postgres.
- `Flask-SQLAlchemy` – A Flask extension that provides support for SQLAlchemy.
- `Flask-Migrate` – Offers SQLAlchemy database migrations for Flask apps using Alembic.

## Installation
First clone this repository
```
$ git clone @https://github.com/hadijahkyampeire/Maintainance-Tracker/tree/flask-api-1
$ cd maintainance-tracker
```
Create virtual environment and install it
```
$ virtualenv --python=python3 venv
$ source /venv/bin/activate
```
Then install all the necessary dependencies by
```
pip install -r requirements.txt
## Run the server
At the terminal or console type
```
python run.py
```
## Testing and knowing coverage
To run tests run this command at the console/terminal
```
nosetests or
python manage.py test
```
To run tests with coverage run this command at the console/terminal
```
python manage.py test_cov or
nosetests -v --with-coverage
```
## Functionality
  End points | Functionality | Access
  ------------------|------------------|--------------------
  /api/v1/auth/signup|Post, create account|PUBLIC
  /api/v1/auth/login|post, login|PUBLIC 
  /api/v1/users/requests |post, add requests|PRIVATE
  /api/v1/users/requests |Get, retrieve all requests| PRIVATE
  /api/v1/users/requests/id|Get, retrieve one request|PRIVATE
  /api/v1/users/requests/id|Put, Edit a request| PRIVATE
  /api/v1/users/requests/id|Delete, Delete a request| PRIVATE
  -----------------|-----------------------|-------------------



   Test your setup using a client app like postman