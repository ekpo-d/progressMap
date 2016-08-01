from flask import render_template, abort, flash, redirect, url_for
from flask_login import login_required, current_user
from . import questions, forms
from .. import models

@login_required
def exportCurrentUser():
	user = current_user
	return user

@questions.route('/')
def show():
	allQuestions = models.getFromDb(models.Questions, 6)
	allComments = models.getFromDb2(models.Comments, 6)
	return render_template('questions.html', allQuestions=allQuestions, allComments=allComments)

@questions.route('/<page>', methods=['GET', 'POST'])
def view(page):
	if page == 'ask':
		return redirect(url_for('questions.ask'))
	if page == '':
		return redirect(url_for('questions.show'))
	
	question = models.getByTitle(models.Questions, page)
	comments = models.getComments(question)
	
	form = forms.commentForm()
	
	if form.validate_on_submit():
		message = form.message.data
		row = models.Comments( message=message, question=question, user=exportCurrentUser())
		models.dbCommit(row)
		
		comments = models.getComments(question)
		
		flash('Reply added')
		return render_template('showQuestion.html', question=question, comments=comments, form=form)
	
	return render_template('showQuestion.html', question=question, comments=comments, form=form)
	
	
@questions.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
	form = forms.askForm()
	if form.validate_on_submit():
		title = form.title.data
		articleTitle = models.returnDbObject(models.Articles, form.article.data.lower())
		message = form.message.data
		
		if articleTitle:
			row = models.Questions(title=title, article=articleTitle, message=message, user=current_user)
			models.dbCommit(row)
		else:
			flash('Sorry the article title you are trying to add to doesn\'t exist!')
			return render_template('ask.html', form=form)
		
		flash("Added a new question")
		return redirect(url_for('questions.show'))
		
	return render_template('ask.html', form = form)
