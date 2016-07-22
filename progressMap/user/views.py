from flask import render_template
from . import user
from .. import models

@user.route('/<username>')
def userPage(username):
	user = models.User.query.filter_by(username=username).first_or_404()
	return render_template('user.html', user = user)