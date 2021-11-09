from flask import request
import pytest
import pdb

from flaskr import create_app
from flaskr import GameModel

game_model = GameModel(name="Thirsty Sword Lesbians",
                  author="April Kit Walsh",
                  image_url="https://img.itch.zone/aW1nLzYxMjUyODYuanBn/347x500/Bnmn5s.jpg",
                  type="TTRPG")

app = create_app()

@pytest.fixture(autouse=False)
def db():
    # Setup DB here

    # Yield some data, database connection or nothing at all
    yield None

    # Delete DB here when the test ends

def test_game_entry_post():
    with app.test_client() as test_client:
        response = test_client.post('/game_entry',  data=dict(name="Thirsty Sword Lesbians",
                                                    author="April Kit Walsh",
                                                    image_url="https://img.itch.zone/aW1nLzYxMjUyODYuanBn/347x500/Bnmn5s.jpg",
                                                    type="TTRPG"))
        assert response.status_code == 302

from flaskr.routes import *
