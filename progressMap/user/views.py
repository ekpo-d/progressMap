from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_required
from . import user
from .. import models


@login_required
@user.route('/<username>')
def userPage(username):
	user = current_user
	usersContent = []
	allContent = models.getAllObjectsById2(models.AllContent, int(user.id))
	return render_template('user.html', user = user, allContent=allContent)

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
	userContent = models.AllContent.query.filter_by(user_id = int(current_user.id)).all()
	newContent= []
	for article in articles:
		for content in userContent:
			if content.article_id == article.id:
				break
		else:
			row = models.AllContent(user=current_user, article=article)
			models.dbCommit(row)
			newContent.append(article)
	
	print newContent
	
	flash('Added all articles under \'{}\' to your account'.format(courseName))
	return redirect(endPoint)

@user.route('/<username>/addArticleContent/<articleName>/<id>/<endPoint>/<path>')
@login_required
def addArticleContent(username, articleName, id, endPoint, path):
	if path == 'return':
		endPoint = '/' + endPoint + '/'
	else:
		endPoint = '/' + endPoint + '/' + path
	article = models.getByTitle(models.Articles, articleName)
	if models.AllContent.query.filter_by(article_id = article.id).first():
		flash('This content has already been added')
		return redirect(endPoint)
	else:
		row = models.AllContent(user=current_user, article=article)
		models.dbCommit(row)
		flash('Added article \'{}\' to your account'.format(articleName))
		return redirect(endPoint)