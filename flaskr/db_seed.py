import click
from flask import Flask
from __init__ import app
from flaskr.models import GameModel

db = app.db

game_models = [GameModel(name="Thirsty Sword Lesbians", author="April Kit Walsh", image_url="https://img.itch.zone/aW1nLzYxMjUyODYuanBn/347x500/Bnmn5s.jpg", type="TTRPG"),
               GameModel(name="Bubblegumshoe", author="Emily Care Boss, Kenneth Hite, Lisa Steele", image_url="https://img.itch.zone/aW1nLzI1NTEwNjUuanBn/347x500/u5fnQi.jpg", type="TTRPG"),
               GameModel(name="Monster of the Week", author="Michael Sands", image_url="https://img.itch.zone/aW1nLzI1NDE2NzQuanBn/347x500/C5VMe6.jpg", type="TTRPG")]

@click.command()
def seed():
    for model in game_models:
        db.session.add(model)
        db.session.commit()

if __name__ == '__main__':
    seed()
