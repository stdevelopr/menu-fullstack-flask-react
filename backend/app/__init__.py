from flask import Flask, Blueprint, render_template
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma




def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db/stdev"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api_bp = Blueprint('api', __name__)
    api = swagger.docs(Api(api_bp), apiVersion='0.1')

    # load the test config if passed in
    if test_config:
        app.config.from_mapping(test_config)

    # external config
    config_db(app)
    config_ma(app)
    Migrate(app, app.db)

    # routes config
    from .resources import clientes, pedidos
    api.init_app(app)
    api.add_resource(clientes.Clientes, '/clientes')
    api.add_resource(clientes.ClienteId, '/clientes/<int:id>')
    api.add_resource(pedidos.Pedidos, '/pedidos')
    api.add_resource(pedidos.PedidoId, '/pedidos/<int:id>')
    app.register_blueprint(api_bp)

    @app.route('/')
    def hello():
        return render_template('index.html')

    return app