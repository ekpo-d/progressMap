from flask import render_template
from . import courses

@courses.route('/')
def show():
	return render_template('courses.html')