from flask import render_template, abort
from . import questions


@questions.route('/')
def show():
	return render_template('questions.html')

@questions.route('/ask')
def ask():
	return render_template('ask.html')