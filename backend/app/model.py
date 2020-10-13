from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_restful_swagger import swagger

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

@swagger.model
class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(20))
    ultimo_nome = db.Column(db.String(20))
    email = db.Column(db.String(40))
    pedidos = db.relationship("Pedido", cascade="all, delete")

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(100))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    valor = db.Column(db.Float)