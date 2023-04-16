from .model import *

def test_is_Base_not_Nothing():
	assert Base is not None

def test_is_DbModel_not_Nothing():
	assert DbModel('','') is not None

def test_is_DbModel_id_set():
	obj = DbModel('test-name','test-color')
	obj.id = 0
	assert obj.id == 0

def test_is_DbModel_name_set():
	obj = DbModel('test-name','test-color')
	assert obj.name == 'test-name'

def test_is_DbModel_color_set():
	obj = DbModel('test-name','test-color')
	assert obj.color == 'test-color'
