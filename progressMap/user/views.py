from flask import render_template
from flask_login import current_user, login_required
from . import user
from .. import models

@login_required
@user.route('/<username>')
def userPage(username):
	user = current_user
	return render_template('user.html', user = user)

@login_required
@user.route('/<username>/content')
def addedContent(username):
	user = current_user
	return render_template('addedContent.html', user = user)
