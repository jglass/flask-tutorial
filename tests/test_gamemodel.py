import pytest

from flaskr import create_app
from flaskr import GameModel

model = GameModel(name="Thirsty Sword Lesbians",
                  author="April Kit Walsh",
                  image_url="https://img.itch.zone/aW1nLzYxMjUyODYuanBn/347x500/Bnmn5s.jpg",
                  type="TTRPG")

def test_gamemodel():
    assert isinstance(model, GameModel)

def test_boolean():
    assert model.active is True
