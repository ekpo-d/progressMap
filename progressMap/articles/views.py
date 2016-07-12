from flask import render_template
from . import articles

@articles.route('/')
def show():
	return render_template('articles.html')