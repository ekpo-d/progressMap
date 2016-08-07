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

@user.route('/<username>/addCourseContent/<courseName>/<id>/<endPoint>/<path>')
@login_required
def addCourseContent(username, courseName, id, endPoint, path):
	if path == 'return':
		endPoint = '/' + endPoint + '/'
	else:
		endPoint = '/' + endPoint + '/' + path
	articles = models.getAllObjectsById(models.Articles, id)
	for article in articles:
		row = models.AllContent(user=current_user, article=article)
		models.dbCommit(row)
	flash('Added all articles under \'{}\' to your account'.format(courseName))
	return redirect(endPoint)

@user.route('/<username>/addCourseContent/<articleName>/<id>/<endPoint>/<path>')
@login_required
def addArticleContent(username, articleName, id, endPoint, path):
	if path == 'return':
		endPoint = '/' + endPoint + '/'
	else:
		endPoint = '/' + endPoint + '/' + path
	article = models.getByTitle(models.Articles, articleName)
	row = models.AllContent(user=current_user, article=article)
	models.dbCommit(row)
	flash('Added article \'{}\' to your account'.format(articleName))
	return redirect(endPoint)