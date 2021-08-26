import os
import psycopg2
import pdb
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import render_template
from .models import CarsModel
from .models import GamesModel


from dotenv import load_dotenv
load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config["DATABASE_USER"]     = os.environ.get("DATABASE_USER")
    app.config["DATABASE_PASSWORD"] = os.environ.get("DATABASE_PASSWORD")
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
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{app.config['DATABASE_USER']}:{app.config['DATABASE_USER']}@localhost/flask_example"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# a simple page that says hello
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# Imports and CarsModel truncated
@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cars = CarsModel.query.all()
        results = [
            {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            } for car in cars]

        return {"count": len(results), "cars": results}
