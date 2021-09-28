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

## Db migration
- python3 flaskr/models.py db init
- flask db migrate
- flask db upgrade

## TODO
- Add show page
- Add delete functionality
- Add update functionality
- Add tests for CRUD
- Add styling
- Add authorization/authentication (Devise-like)
- Deploy to Heroku
