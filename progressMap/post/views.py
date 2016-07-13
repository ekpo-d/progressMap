from flask import render_template, abort
from . import post


@post.route('/add')
def add():
	return render_template('add.html')

@post.route('/ask')
def ask():
	return render_template('ask.html')