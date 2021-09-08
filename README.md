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

<!-- INSERT INTO films (code, title, did, date_prod, kind) VALUES
    ('B6717', 'Tampopo', 110, '1985-02-10', 'Comedy'),
    ('HG120', 'The Dinner Game', 140, DEFAULT, 'Comedy'); -->

    <!-- INSERT INTO games (name, author, type, image_url) VALUES
        ('Fate of Cthulhu', 'Stephen Blackmoor', 'ttrpg', 'https://img.itch.zone/aW1hZ2UvNTQ3MjM2LzI4NTc3NzQuanBn/original/0wWvO3.jpg'),
        ('Bubblegumshoe', 'Emily Care Boss', 'ttrpg', 'https://img.itch.zone/aW1nLzI1NTEwNjUuanBn/original/KPZdct.jpg');

    INSERT INTO games (name, author, type, image_url) VALUES
        ('Asteroids', 'Atari', 'arcade', 'https://www.arcade-museum.com/images/118/118124204993.jpg'),
        ('Ms Pac Man', 'Midway', 'arcade', 'https://www.arcade-museum.com/images/118/1181242138311.jpg'),
        ('Galaga', 'Namco', 'arcade', 'https://www.arcade-museum.com/images/G/aGalaga.jpg'),
        ('Frogger', 'Sega/Gremlin', 'arcade', 'https://www.arcade-museum.com/images/118/118124210849.jpg'); -->
