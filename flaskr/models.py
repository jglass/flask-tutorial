import os
from flask import Flask
from flask_migrate import Migrate
from .__init__ import app

db = app.db

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
