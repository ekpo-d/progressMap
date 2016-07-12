from flask import render_template, abort
from . import main

@main.route('/', defaults={'page' : 'index'})
@main.route('/<page>')
def show(page):
	if page == 'index':
		return render_template('index.html')
	elif page == 'login':
		return render_template('signin.html')
	elif page == 'signup':
		return render_template('signup.html')
	elif page == 'map':
		return render_template('map.html')
	else:
		abort(404)

	
@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500