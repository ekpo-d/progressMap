from flask import render_template, abort
from . import add, forms


@add.route('/')
def main():
	form = forms.addForm()
	return render_template('add.html', form = form)