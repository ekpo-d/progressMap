from flask import render_template, abort
from . import questions, forms


@questions.route('/')
def show():
	return render_template('questions.html')

@questions.route('/ask', methods=['GET', 'POST'])
def ask():
	form = forms.askForm()
	return render_template('ask.html', form = form)