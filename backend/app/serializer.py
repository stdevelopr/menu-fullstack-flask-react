from flask_marshmallow import Marshmallow
from .model import Cliente

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class ClienteSchema(ma.Schema):
    class Meta:
        model = Cliente
        fields = ('id','primeiro_nome', 'ultimo_nome', 'email')

class PedidoSchema(ma.Schema):
    class Meta:
        model = Cliente
        fields = ('id', 'data', 'status', 'cliente_id', 'valor')