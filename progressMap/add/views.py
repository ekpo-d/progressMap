from flask import render_template, abort, flash, redirect, url_for
from flask_login import login_required, current_user
from . import add, forms
from .. import models, db

def returnDbObject(dbtable, title):
	if models.getByTitle(dbtable, title):
		title = models.getByTitle(dbtable, title)
		return title
	
def refreshOnError(fieldTitle, template, form):
	flash('Sorry the {} you are trying to add to doesn\'t exist!'.format(fieldTitle) )
	return render_template(template, form=form)

def dbCommit(row):
	db.session.add(row)
	db.session.commit()

@add.route('/')
def main():
	return render_template('add.html')

@add.route('/article', methods=['GET', 'POST'])
@login_required
def article():
	form = forms.articleForm()
	if form.validate_on_submit():
		title = form.title.data
		course = returnDbObject(models.Courses, form.course.data)
		curriculum = returnDbObject(models.Curriculums, form.curriculum.data)
		description = form.description.data
		
		if course and curriculum:
			row = models.Articles(title=title, course=course, curriculum=curriculum, description=description, user=current_user)
			dbCommit(row)
		else:
			return refreshOnError('curriculum or course', 'addArticle.html', form)			
		
		flash("Added article '{}'.".format(form.title.data))
		return redirect(url_for('articles.show'))
	return render_template('addArticle.html', form=form)

@add.route('/course', methods=['GET', 'POST'])
def course():
	form = forms.courseForm()
	if form.validate_on_submit():
		title = form.title.data
		description = form.description.data
		curriculum = returnDbObject(models.Curriculums, form.curriculum.data)
		if curriculum:
			row = models.Courses(title=title, curriculum=curriculum, description=description, user=current_user)
			dbCommit(row)
		else:
			return refreshOnError('curriculum', 'addCourse.html', form)
		
		flash("Added course '{}'.".format(form.title.data))
		return redirect(url_for('courses.show'))
	return render_template('addCourse.html', form=form)

@add.route('/curriculum', methods=['GET', 'POST'])
def curriculum():
	form = forms.curriculumForm()
	if form.validate_on_submit():
		title = form.title.data
		description = form.description.data
		row = models.Curriculums(title=title, description=description, user=current_user)
		dbCommit(row)
		
		flash("Added curriculum '{}'.".format(form.title.data))
		return redirect(url_for('curriculums.show'))
	return render_template('addCurriculum.html', form=form)