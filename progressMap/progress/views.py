from flask import render_template
from . import progress

@progress.route('/<user>')
def user(user):
	return render_template('progress.html', user = user)