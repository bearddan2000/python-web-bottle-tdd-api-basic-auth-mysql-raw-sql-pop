from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import delete, update

from .connection.chained import get_db
from .model import DbModel
from .strategy.cls_chained import *

KEY = 'results'
FIELDS = ['test-name', 'test-color']

def get_strategy():
    db: sessionmaker = next(get_db())
    return Chained(db)

def test_all_has_key():
    o = get_strategy()
    res = o.all()
    assert KEY in res
    
def test_all_count():
    o = get_strategy()
    res = o.all()[KEY]
    assert len(res) == 4

def test_commit_refresh_statement_value():
    index = 1
    stm = update(DbModel) \
        .where(DbModel.id == index) \
        .values(name=FIELDS[0],color=FIELDS[1])
    o = get_strategy()
    before = o.all()[KEY][0]
    after =  o.commit_refresh(stm)[KEY][0]
    assert before != after

def test_commit_refresh_statement_query_value():
    index = 1
    args = {"pop_id": int(index)}
    stm = delete(DbModel).where(DbModel.id == index)
    o = get_strategy()
    before = o.all()[KEY][0]
    after =  o.commit_refresh(stm,args)[KEY][0]
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
