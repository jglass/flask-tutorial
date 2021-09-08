import os
import psycopg2
import pdb
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import render_template
from .models import GamesModel
from sqlalchemy.sql import select
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

# boardgames
@app.route('/board_games')
def hello(name=None):
    return render_template('hello.html', name=name)


# Imports and GamesModel truncated
@app.route('/games', methods=['POST', 'GET'])
def handle_games():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_game = GamesModel(name=data['name'], author=data['author'], image_url=data['image_url'])
            db.session.add(new_game)
            db.session.commit()
            return {"message": f"game {new_game.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        type = request.args.get('type')

        if type == 'board_game':
            games = GamesModel.query.filter(GamesModel.type=='board_game')
        elif type == 'arcade':
            games = GamesModel.query.filter(GamesModel.type=='arcade')
        elif type == 'ttrpg':
            games = GamesModel.query.filter(GamesModel.type=='ttrpg')
        else:
            games = GamesModel.query.all()
        results = [
            {
                "name": game.name,
                "author": game.author,
                "image_url": game.image_url
            } for game in games]

        return render_template('games.html', games=results)
