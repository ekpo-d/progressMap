from flask import render_template
from . import user

@user.route('/<username>')
def userPage(username):
	return render_template('progress.html', username = username)