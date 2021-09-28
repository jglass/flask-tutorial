import os
import psycopg2
import pdb
from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import GameModel
from sqlalchemy.sql import *
#from .models import CarsModel

from dotenv import load_dotenv
load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config["DATABASE_USER"]     = os.environ.get("DATABASE_USER")
    app.config["DATABASE_PASSWORD"] = os.environ.get("DATABASE_PASSWORD")
    app.config["DATABASE_NAME"] = os.environ.get("DATABASE_NAME")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{app.config['DATABASE_USER']}:{app.config['DATABASE_PASSWORD']}@localhost/{app.config['DATABASE_NAME']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'supersecretkey'

    db = SQLAlchemy(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{app.config['DATABASE_USER']}:{app.config['DATABASE_PASSWORD']}@localhost/{app.config['DATABASE_NAME']}"
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from flaskr.routes import *
