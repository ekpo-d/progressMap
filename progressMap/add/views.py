from flask import render_template, abort, flash, redirect, url_for
from flask_login import login_required, current_user
from . import add, forms


def refreshOnError(fieldTitle, template, form):
    flash('Sorry the {} you are trying to add to doesn\'t exist!'.format(fieldTitle))
    return render_template(template, form=form)


@add.route('/')
def main():
    return render_template('add.html')


@add.route('/article', methods=['GET', 'POST'])
@login_required
def article():
    form = forms.articleForm()
    if form.validate_on_submit():
        status, title = form.save(current_user)
        if not status:
            return refreshOnError('curriculum or course', 'addArticle.html', form)

        flash("Added article '{}'.".format(title))
        return redirect(url_for('articles.show'))
    return render_template('addArticle.html', form=form)


@add.route('/course', methods=['GET', 'POST'])
def course():
    form = forms.courseForm()
    if form.validate_on_submit():
        status, title = form.save(current_user)
        if not status:
            return refreshOnError('curriculum', 'addCourse.html', form)
        flash("Added course '{}'.".format(title))
        return redirect(url_for('courses.show'))
    return render_template('addCourse.html', form=form)


@add.route('/curriculum', methods=['GET', 'POST'])
def curriculum():
    form = forms.curriculumForm()
    if form.validate_on_submit():
        title = form.save(current_user)
        flash("Added curriculum '{}'.".format(title))
        return redirect(url_for('curriculums.show'))
    return render_template('addCurriculum.html', form=form)
