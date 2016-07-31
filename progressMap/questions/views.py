from flask import render_template, abort
from flask_login import login_required, current_user
from . import questions, forms
from .. import models


@questions.route('/', defaults={'page':'all'})
@questions.route('/<page>')
def show(page):
	if page == 'all':
		allQuestions = models.getFromDb2(models.Questions, 6)
		return render_template('questions.html', allQuestions=allQuestions)
	elif page ==  models.getByTitle(models.Questions, page).message:
		question = models.getByTitle(models.Questions, page)
		return render_template('showQuestion.html', question=question)
	else:
		abort(404)
	
@questions.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
	form = forms.askForm()
	if form.validate_on_submit():
		title = form.title.data
		articleTitle = models.returnDbObject(models.Articles, form.article.data.lower())
		message = form.message.data
		
		if articleTitle:
			row = models.Questions(article=articleTitle, message=message, user=current_user)
			models.dbCommit(row)
		else:
			flash('Sorry the article title you are trying to add to doesn\'t exist!')
			return render_template('ask.html', form=form)
		
		flash("Added a new question")
		return redirect(url_for('questions.show'))
		
	return render_template('ask.html', form = form)
