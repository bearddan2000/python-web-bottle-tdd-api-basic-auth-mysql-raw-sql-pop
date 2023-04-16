import bottle
from bottle import auth_basic, route, run, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from connection.prod import engine, session_local
from connection.api import get_db

from model import Base
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

def setup_routes():
     bottle.route('/pop/<pop_id>', ['GET', 'DELETE'], crud)
     bottle.route('/pop/<pop_name>/<pop_color>', ['PUT'], insert_entry)
     bottle.route('/pop/<pop_id>/<pop_name>/<pop_color>', ['POST'], update_entry)
     
     # for api testing
     bottle.route('/api/pop', ['GET'], api_get_all)
     bottle.route('/api/pop/<pop_id>', ['GET', 'DELETE'], api_crud)
     bottle.route('/api/pop/<pop_name>/<pop_color>', ['PUT'], api_insert_entry)
     bottle.route('/api/pop/<pop_id>/<pop_name>/<pop_color>', ['POST'], api_update_entry)

def get_strategy(db):
     return Raw(db)

def is_authenticated_user(user, password):
    # You write this function. It must return
    # True if user/password is authenticated, or False to deny access.
	if user == 'user' and password == 'pass':
		return True
	return False

@route('/')
def hello():
	return {"hello": "world"}

@route('/api')
def api_hello():
	return {"hello": "world"}

@route('/pop')
@auth_basic(is_authenticated_user)
def get_all(db):
    strategy = get_strategy(db)
    return strategy.all()

@auth_basic(is_authenticated_user)
def api_get_all():
    db = next(get_db())
    strategy = get_strategy(db)
    return strategy.all()

@auth_basic(is_authenticated_user)
def crud(db, pop_id):
    strategy = get_strategy(db)
    if request.method == 'GET':
        return strategy.filter_by(pop_id)
    
    return strategy.delete_by(pop_id)

@auth_basic(is_authenticated_user)
def api_crud(pop_id):
    db = next(get_db())
    strategy = get_strategy(db)
    if request.method == 'GET':
        return strategy.filter_by(pop_id)
    
    return strategy.delete_by(pop_id)

@auth_basic(is_authenticated_user)
def insert_entry(db, pop_name, pop_color):
    strategy = get_strategy(db)
    return strategy.insert_entry(pop_name, pop_color)

@auth_basic(is_authenticated_user)
def api_insert_entry(pop_name, pop_color):
    db = next(get_db())
    strategy = get_strategy(db)
    return strategy.insert_entry(pop_name, pop_color)

@auth_basic(is_authenticated_user)
def update_entry(db, pop_id, pop_name, pop_color):
    strategy = get_strategy(db)
    return strategy.update_entry(pop_id, pop_name, pop_color)

@auth_basic(is_authenticated_user)
def api_update_entry(pop_id, pop_name, pop_color):
    db = next(get_db())
    strategy = get_strategy(db)
    return strategy.update_entry(pop_id, pop_name, pop_color)

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=False, create_session = session_local))

setup_routes()

run(host='0.0.0.0', port=8000,debug=True)
