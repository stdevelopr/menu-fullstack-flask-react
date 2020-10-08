
from flask import current_app, request, jsonify
from flask_restful import Resource
from app.model import Pedido
from app.serializer import PedidoSchema

class Pedidos(Resource):
    def get(self):
        ps = PedidoSchema(many=True)
        result = Pedido.query.all()
        return ps.jsonify(result)

    def post(self):
        json_data = request.get_json()
        ps = PedidoSchema()
        if not json_data:
            return {"message": "Dados de entrada não fornecidos"}, 400
        # Validate and deserialize input
        try:
            data = ps.load(json_data)
        except Exception as err:
            return err.messages, 422
        
        novo_pedido = Pedido(**data)

        current_app.db.session.add(novo_pedido)
        current_app.db.session.commit()

        result = ps.dump(Pedido.query.get(novo_pedido.id))
        return {"message": "Criado novo pedido.", "pedido": result}

    
class PedidoId(Resource):
    def get(self, id):
        ps = PedidoSchema()
        result = Pedido.query.get(id)

        return ps.jsonify(result)
    
    def put(self, id):
        json_data = request.get_json()
        ps = PedidoSchema()

        # Validate and deserialize input
        try:
            data = ps.load(json_data)
        except Exception as err:
            return err.messages, 422

        query = Pedido.query.filter_by(id=id)
        query.update(data)
        current_app.db.session.commit()
        
        return ps.jsonify(query.first())

    def delete(self, id):
        Pedido.query.filter_by(id=id).delete()
        current_app.db.session.commit()
        return jsonify('Deletado!')