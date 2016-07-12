from flask import render_template, abort
from . import post


@post.route('/', defaults={'page' : 'ask'})
@post.route('/<page>')
def show(page):
	if page == 'ask':
		return render_template('ask.html')
	elif page == 'add':
		return render_template('add.html')
	else:
		abort(404)