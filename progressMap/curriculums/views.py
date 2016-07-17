from flask import render_template
from . import curriculums

@curriculums.route('/')
def show():
	return render_template('curriculums.html')