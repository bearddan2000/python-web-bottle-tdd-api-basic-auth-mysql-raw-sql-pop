from .app import *

def test_is_authenticated_user_true():
	assert is_authenticated_user('user', 'pass') == True

def test_is_authenticated_user_false():
	assert is_authenticated_user('', '') == False
