from .__init__ import app
from flask import request, render_template, redirect, flash
from .models import GameModel
from .helpers import GamesForm
from .helpers import LoginForm
from sqlalchemy import insert

import pdb
import flask_login

login_manager = flask_login.LoginManager()

login_manager.init_app(app)


db = app.db

# Imports and GameModel truncated
@app.route('/games', methods=['POST', 'GET'])
def handle_games():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_game = GameModel(name=data['name'], author=data['author'], image_url=data['image_url'])
            db.session.add(new_game)
            db.session.commit()
            return {"message": f"game {new_game.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        type = request.args.get('type')

        if type == 'board_game':
            games = GameModel.query.filter(GameModel.type=='board_game')
        elif type == 'arcade':
            games = GameModel.query.filter(GameModel.type=='arcade')
        elif type == 'ttrpg':
            games = GameModel.query.filter(GameModel.type=='ttrpg')
        else:
            games = GameModel.query.all()
        results = [
            {
                "name": game.name,
                "author": game.author,
                "image_url": game.image_url
            } for game in games]

        return render_template('games.html', games=results)

@app.route('/game_entry', methods=['GET', 'POST'])
def game_entry():
    form = GamesForm(request.form)
    if request.method == 'POST' and form.validate():
        stmt = (insert(GameModel.__table__).values(name=form.name.data, author=form.author.data, image_url=form.image_url.data, type=form.type.data))
        compiled = stmt.compile()
        conn = db.session.connection()
        result = conn.execute(stmt)
        db.session.commit()

        flash('Game successfully added')
        return redirect('/games')

    return render_template('game_entry.html', form=form)

users = {'foo@bar.tld': {'password': 'secret'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('login.html', form=form)
