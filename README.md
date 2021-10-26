### Setup

- Install Python 3.9.5
- Follow instructions here[https://flask.palletsprojects.com/en/2.0.x/installation/]
- Setup for DB here[https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/]

## Virtual environments
- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

### Initially
- python3 -m venv venv

### After that
- source venv/bin/activate

### Install Packages
- pip install -r requirements.txt

### Create .env file
- cp .env.example .env
- add required environmental variables to .env file

## Db migration
- flask db stamp head (if starting from scratch)
- flask db migrate
- flask db upgrade

## Add to Database
https://www.postgresql.org/docs/9.5/sql-insert.html

## TODO
- Add show page
- Add delete functionality
- Add update functionality
- Add tests for CRUD
- Add styling
- Add authorization/authentication (Devise-like)
- Deploy to Heroku
