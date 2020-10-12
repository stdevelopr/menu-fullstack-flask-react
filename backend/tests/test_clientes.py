import json
from app.serializer import ClienteSchema
from app.common.utils import clean_null_values_from_json

cs = ClienteSchema()

def test_get_clientes(client):
    resp = client.get('/clientes')
    assert resp.status_code == 200

def test_get_clientes_sort_range(client):
    resp = client.get('/clientes?sort=["id", "ASC"]&range=[1,10]')
    assert resp.status_code == 200

def test_post_clientes_no_data(client):
    resp = client.post('/clientes')
    assert resp.status_code == 400
    assert resp.content_type == "application/json"

def test_post_clientes_valid_json(client):
    valid_client = {
        "primeiro_nome": "ok",
        "ultimo_nome": "ok",
        "email": "ok"
    }
    resp = client.post('/clientes', headers={'Content-Type': 'application/json'}, data=json.dumps(valid_client))
    assert resp.status_code == 200


def test_post_clientes_invalid_json(client):
    resp = client.post('/clientes', headers={'Content-Type': 'application/json'}, data=json.dumps({'test':'invalid'}))
    assert resp.status_code == 422

def test_clientes_id_get(client, cliente_id):
    resp = client.get(f'/clientes/{cliente_id}')
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert resp.json['primeiro_nome'] == "Testing client"

def test_clientes_id_put_no_data(client, cliente_id):
    resp = client.put(f'/clientes/{cliente_id}')
    assert resp.status_code == 400

def test_clean_json_null_values(client, cliente_id):
    json_client = {
        "primeiro_nome": "OK",
        "ultimo_nome": None,
        "email": None
    }
    resp_json = clean_null_values_from_json(json_client)
    assert resp_json == {"primeiro_nome" : "OK"}


def test_clientes_id_put_invalid_json(client, cliente_id):
    put_client = {
        "prime_nome": "OK",
        "ultimo_nome": None,
        "email": None
    }
    resp = client.put(f'/clientes/{cliente_id}', headers={'Content-Type': 'application/json'}, data=json.dumps(put_client))
    assert resp.status_code == 422

def test_clientes_id_put_valid_json(client, cliente_id):
    put_client = {
        "primeiro_nome": "OK",
        "ultimo_nome": None,
        "email": None
    }
    resp = client.put(f'/clientes/{cliente_id}', headers={'Content-Type': 'application/json'}, data=json.dumps(put_client))
    assert resp.json['primeiro_nome'] == "OK"


def test_clientes_id_delete(client, cliente_id):
    resp = client.delete(f'/clientes/{cliente_id}')
    assert resp.status_code == 200
    assert resp.json['cliente']['id'] == cliente_id 
    assert resp.json['cliente']['primeiro_nome'] == "Testing client" 
    assert resp.json['msg'] == 'Deletado!'






