from testing.postgresql import Postgresql

import pytest
from app import create_app
from app.model import db as _db, Cliente

@pytest.yield_fixture(scope='session')
def app():
    _app = create_app({
        'TESTING': True,
        'ENV': 'test',
        'DEBUG': True
    })
    with Postgresql() as postgresql:
        _app.config['SQLALCHEMY_DATABASE_URI'] = postgresql.url()
        _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        ctx = _app.app_context()
        ctx.push()

        yield _app

        ctx.pop()

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
    

@pytest.yield_fixture(scope='session')
def db(app):
    _db.app = app
    _db.create_all()

    yield _db

    _db.drop_all()


@pytest.fixture(scope='function', autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)

    db.session = session_

    yield session_

    transaction.rollback()
    connection.close()
    session_.remove()



@pytest.yield_fixture(scope='function', autouse=True)
def cliente_id(session):
    new_client = Cliente(primeiro_nome="Testing client")
    session.add(new_client)
    session.commit()

    return new_client.id