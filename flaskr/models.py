import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from .__init__ import app
from flask_login import UserMixin

db = app.db
migrate = Migrate(app, db)

class GameModel(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    image_url = db.Column(db.String())
    type = db.Column(db.String())

    def __init__(self, name, author, image_url, type):
        self.name     = name
        self.author   = author
        self.image_url = image_url
        self.type     = type

    def __repr__(self):
        return f"<Game {self.name}>"

class UserModel(db.Model):
    __tablename__ = 'users'

    id       = db.Column(db.Integer, primary_key=True)
    email    = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, email, password):
        self.email    = email
        self.password = password

    def __repr__(self):
        return f"<User {self.email}>"
