from flask import Flask, Blueprint, render_template
from flask_restful import Api
from flask_migrate import Migrate
from .model import configure as config_db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db/stdev"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # external config
    config_db(app)
    Migrate(app, app.db)

    return app