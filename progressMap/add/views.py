from flask import render_template, abort, flash, redirect, url_for
from flask_login import login_required, current_user
from . import add, forms
from .. import models, db

@add.route('/')
def main():
	return render_template('add.html')

@add.route('/article', methods=['GET', 'POST'])
@login_required
def article():
	form = forms.articleForm()
	if form.validate_on_submit():
		title = form.title.data
		course = form.course.data
		curriculum = form.curriculum.data
		description = form.description.data
		row = models.Articles(title=title, course=course, curriculum=curriculum, description=description, user=current_user)
		db.session.add(row)
		db.session.commit()
		
		flash("Added article '{}'.".format(form.title.data))
		return redirect(url_for('articles.show'))
	return render_template('addArticle.html', form=form)

@add.route('/course', methods=['GET', 'POST'])
def course():
	form = forms.courseForm()
	if form.validate_on_submit():
		flash("Added course '{}'.".format(form.title.data))
		return redirect(url_for('courses.show'))
	return render_template('addCourse.html', form=form)

@add.route('/curriculum', methods=['GET', 'POST'])
def curriculum():
	form = forms.curriculumForm()
	if form.validate_on_submit():
		flash("Added curriculum '{}'.".format(form.title.data))
		return redirect(url_for('curriculums.show'))
	return render_template('addCurriculum.html', form=form)