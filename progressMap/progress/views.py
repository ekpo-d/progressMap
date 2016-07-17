from flask import render_template
from . import progress

@progress.route('/<username>')
def userPage(username):
	return render_template('progress.html', username = username)