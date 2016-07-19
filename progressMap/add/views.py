from flask import render_template, abort, flash, redirect, url_for
from . import add, forms
from .. import models


@add.route('/', methods=['GET', 'POST'])
def main():
	form = forms.addForm()
	if form.validate_on_submit():
		title = forms.title.data
		select = forms.select.data
		description = forms.description.data
		article = models.Article(title=title, )
		flash("Stored '{}'".format(form.title.data) )
		return redirect(url_for('articles.show'));
	return render_template('add.html', form = form)