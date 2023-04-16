from bottle import auth_basic, request, route, run

def is_authenticated_user(user, password):
    # You write this function. It must return
    # True if user/password is authenticated, or False to deny access.
	if user == 'user' and password == 'pass':
		return True
	return False

@route('/')
@auth_basic(is_authenticated_user)
def index():
	return {'results': 'hello world'}

# run(host='0.0.0.0', port=8000,debug=True)
