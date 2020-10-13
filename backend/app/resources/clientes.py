
from flask import current_app, request, jsonify
from flask_restful import Resource, reqparse
from flask_restful_swagger import swagger
from app.model import Cliente
from app.serializer import ClienteSchema
from app.common.utils import clean_null_values_from_json
import json

cs = ClienteSchema()
csm = ClienteSchema(many=True)

class Clientes(Resource):
    "Clientes"
    @swagger.operation(
        notes='Retorna todos os clientes.',
        nickname='clientes',
        responseMessages=[
            {
              "code": 200,
              "message": "Retorna uma lista com todos os clientes"
            }
          ]
        )
    def get(self):
        # try to get url parameters to sort
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('sort', action='split', type=str)
            parser.add_argument('range', action='split')
            args = parser.parse_args()
            if args['sort']:
                sort = json.loads(args['sort'])
            if args['range']:
                range = json.loads(args['range'])
            print(type(args), args)
            arg = getattr(getattr(Cliente, sort[0]), sort[1].lower())()
            result = Cliente.query.order_by(arg).offset(range[0]).limit(range[1]-range[0]+1).all()
        except:
            result = Cliente.query.order_by('id').all()
        resp_size = Cliente.query.count()
        resp = csm.jsonify(result)
        resp.headers.add( 'Access-Control-Expose-Headers', 'Content-Range')
        resp.headers.add('Content-Range',f'clientes : 0-9/{resp_size}')
        return resp

    "Describing elephants"
    @swagger.operation(
        notes='Cria um novo cliente',
        nickname='post',
        parameters=[
            {
              "name": "body",
              "description": "Cria um novo cliente a partir de um json.",
              "required": True,
              "allowMultiple": False,
              "dataType": json.dumps({"primeiro_nome":"exemplo", "ultimo_nome": "exemplo", "email":"exemplo"}),
              "paramType": "body"
            }
          ],
        responseMessages=[
            {
              "code": 200,
              "message": "Novo cliente criado."
            },
            {
              "code": 400,
              "message": "Dados de entrada não fornecidos"
            },
            {
              "code": 422,
              "message": "Error message"
            }
          ]
        )
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
    "Cliente ID"
    @swagger.operation(
        notes='Retorna um cliente pelo id.',
        nickname='cliente id',
        parameters=[
            {
              "name": "id",
              "description": "Id do cliente.",
              "required": True,
              "allowMultiple": False,
              "dataType": "integer",
              "paramType": "path"
            }
          ],
        responseMessages=[
            {
              "code": 200,
              "message": "Um json contendo as informações do cliente"
            }
          ]
        )
    def get(self, id):
        result = Cliente.query.get(id)
        return cs.jsonify(result)

    "Atualiza Cliente ID"
    @swagger.operation(
        notes='Atualiza as informações de um cliente de dado id.',
        nickname='atualiza cliente id',
        parameters=[
            {
              "name": "id",
              "description": "Id do cliente.",
              "required": True,
              "allowMultiple": False,
              "dataType": "integer",
              "paramType": "path"
            },
            {
              "name": "body",
              "description": "Cria um novo cliente a partir de um json.",
              "required": True,
              "allowMultiple": False,
              "dataType": json.dumps({"primeiro_nome":"exemplo", "ultimo_nome": "exemplo", "email":"exemplo"}),
              "paramType": "body"
            }
          ],
        responseMessages=[
            {
              "code": 200,
              "message": "Um json contendo as novas informações do cliente"
            },
            {
              "code": 422,
              "message": "Error message"
            }
          ]
        )
    
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


    "Deleta Cliente ID"
    @swagger.operation(
        notes='Deleta um cliente pelo id.',
        nickname='deleta cliente id',
        parameters=[
            {
              "name": "id",
              "description": "Id do cliente.",
              "required": True,
              "allowMultiple": False,
              "dataType": "integer",
              "paramType": "path"
            }
          ],
        responseMessages=[
            {
              "code": 200,
              "message": "Deletado!"
            }
          ]
        )

    def delete(self, id):
        client = Cliente.query.filter_by(id=id).first()
        current_app.db.session.delete(client)
        current_app.db.session.commit()
        return jsonify({'msg': 'Deletado!', 'cliente': cs.dump(client)})