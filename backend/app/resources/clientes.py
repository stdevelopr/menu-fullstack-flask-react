
from flask import current_app, request, jsonify
from flask_restful import Resource, reqparse
from app.model import Cliente
from app.serializer import ClienteSchema
from app.common.utils import clean_null_values_from_json
import json

cs = ClienteSchema()
csm = ClienteSchema(many=True)

class Clientes(Resource):
    def get(self):
        # try to get url parameters to sort
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('sort', action='split')
            parser.add_argument('range', action='split')
            args = parser.parse_args()
            if args['sort']:
                sort = json.loads(args['sort'])
            if args['range']:
                range = json.loads(args['range'])
            arg = getattr(getattr(Cliente, sort[0]), sort[1].lower())()
            result = Cliente.query.order_by(arg).offset(range[0]).limit(range[1]-range[0]+1).all()
        except:
            result = Cliente.query.order_by('id').all()
        resp_size = Cliente.query.count()
        resp = csm.jsonify(result)
        resp.headers.add( 'Access-Control-Expose-Headers', 'Content-Range')
        resp.headers.add('Content-Range',f'clientes : 0-9/{resp_size}')
        return resp

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "Dados de entrada não fornecidos"}, 400
        # Validate and deserialize input
        try:
            data = cs.load(json_data)
        except Exception as err:
            return err.messages, 422
        
        new_client = Cliente(**data)

        current_app.db.session.add(new_client)
        current_app.db.session.commit()

        result = cs.dump(Cliente.query.get(new_client.id))
        return {"message": "Novo cliente criado.", "cliente": result}

    
class ClienteId(Resource):
    def get(self, id):
        result = Cliente.query.get(id)

        return cs.jsonify(result)
    
    def put(self, id):
        json_data = request.get_json()

        if not json_data:
            return {"message": "Dados de entrada não fornecidos"}, 400

        json_data = clean_null_values_from_json(json_data)

        # Validate and deserialize input
        try:
            data = cs.load(json_data, partial=True)
        except Exception as err:
            return err.messages, 422

        query = Cliente.query.filter_by(id=id)
        query.update(data)
        current_app.db.session.commit()
        
        return cs.jsonify(query.first())

    def delete(self, id):
        client = Cliente.query.filter_by(id=id).first()
        current_app.db.session.delete(client)
        current_app.db.session.commit()
        return jsonify({'msg': 'Deletado!', 'cliente': cs.dump(client)})