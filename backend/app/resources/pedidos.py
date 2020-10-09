
from flask import current_app, request, jsonify
from flask_restful import Resource, reqparse
from app.model import Pedido
from app.serializer import PedidoSchema
import json

psm = PedidoSchema(many=True)

class Pedidos(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('sort', action='split')
            parser.add_argument('range', action='split')
            args = parser.parse_args()
            sort = json.loads(args['sort'])
            range = json.loads(args['range'])
            print(sort, range)
            arg = getattr(getattr(Pedido, sort[0]), sort[1].lower())()
            result = Pedido.query.order_by(arg).offset(range[0]).limit(range[1]-range[0]+1).all()
        except:
            result = Pedido.query.order_by('id').all()
        resp = psm.jsonify(result)
        resp_size = Pedido.query.count()
        resp.headers.add( 'Access-Control-Expose-Headers', 'Content-Range')
        resp.headers.add('Content-Range',f'clientes : 0-9/{resp_size}')
        return resp

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