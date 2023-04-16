from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from .connection.raw import get_db
from .strategy.cls_raw import *

KEY = 'results'
FIELDS = ['test-name', 'test-color']

def get_strategy():
    db: sessionmaker = next(get_db())
    return Raw(db)

def test_all_has_key():
    o = get_strategy()
    res = o.all()
    assert KEY in res
    
def test_all_count():
    o = get_strategy()
    res = o.all()[KEY]
    assert len(res) == 4

def test_commit_refresh_statement_query_value():
    o = get_strategy()
    index = 1
    args = {"pop_id": index}
    stm = text("DELETE FROM pop WHERE id = :pop_id")
    before = o.all()[KEY][0]
    after =  o.commit_refresh(args,stm)[KEY][0]
    assert before != after

def test_filter_count():
    o = get_strategy()
    res = o.filter_by(pop_id=2)[KEY]
    assert len(res) == 1

def test_insert_value():
    o = get_strategy()
    before = o.all()[KEY]
    after =  o.insert_entry(pop_name=FIELDS[0],pop_color=FIELDS[1])['results']
    assert before != after

def test_update_value():
    o = get_strategy()
    before = o.all()[KEY][1]
    after =  o.update_entry(pop_id=2,pop_name=FIELDS[0],pop_color=FIELDS[1])['results'][0]
    assert before != after

def test_delete_value():
    o = get_strategy()
    before = o.all()[KEY][1]
    after =  o.delete_by(pop_id=2)[KEY][1]
    assert before != after
