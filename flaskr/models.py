import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config["DATABASE_USER"]     = os.environ.get("DATABASE_USER")
app.config["DATABASE_PASSWORD"] = os.environ.get("DATABASE_PASSWORD")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{app.config['DATABASE_USER']}:{app.config['DATABASE_USER']}@localhost/flask_example"
db = SQLAlchemy(app)

class GamesModel(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    image_url = db.Column(db.String())

    def __init__(self, name, author, image_url):
        self.name     = name
        self.author   = author
        self.image_url = image_url

    def __repr__(self):
        return f"<Game {self.name}>"

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"
