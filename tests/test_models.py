import pytest

from flaskr import create_app
from flaskr import GameModel

game_model = GameModel(name="Thirsty Sword Lesbians",
                  author="April Kit Walsh",
                  image_url="https://img.itch.zone/aW1nLzYxMjUyODYuanBn/347x500/Bnmn5s.jpg",
                  type="TTRPG")

def test_gamemodel():
    assert isinstance(game_model, GameModel)
