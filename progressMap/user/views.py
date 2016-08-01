from flask import render_template, request, url_for, redirect, flash
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

@user.route('/<username>/addCourseContent/<courseName>/<id>')
@login_required
def addCourseContent(username, courseName, id):
	articles = models.getAllObjectsById(models.Articles, id)
	for article in articles:
		row = models.AllContent(user=current_user, article=article)
		models.dbCommit(row)
	flash('Added all articles under \'{}\' to your account'.format(courseName))
	return redirect(url_for('courses.show'))
