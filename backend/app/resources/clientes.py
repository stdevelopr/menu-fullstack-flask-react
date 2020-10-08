
from flask import current_app, request, jsonify
from flask_restful import Resource
from app.model import Cliente
from app.serializer import ClienteSchema

cs = ClienteSchema()
csm = ClienteSchema(many=True)

class Clientes(Resource):
    def get(self):
        result = Cliente.query.all()
        return csm.jsonify(result)

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

        # Validate and deserialize input
        try:
            data = cs.load(json_data)
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
        return jsonify('Deletado!')