from flask import render_template, abort
from flask_login import login_required, current_user
from . import questions, forms
from .. import models


@questions.route('/')
def show():
	return render_template('questions.html')

@questions.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
	form = forms.askForm()
	if form.validate_on_submit():
		articleTitle = models.returnDbObject(models.Articles, form.title.data.lower())
		message = form.message.data
		
		if title:
			row = models.Questions(article=articleTitle, message=message, user=current_user)
			models.dbCommit(row)
		else:
			flash('Sorry the article title you are trying to add to doesn\'t exist!')
			return render_template('ask.html', form=form)
		
	return render_template('ask.html', form = form)
