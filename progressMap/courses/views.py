from flask import render_template
from . import courses
from .. import models

@courses.route('/')
def show():
	coursesList = models.getFromDb(models.Courses, 6)
	return render_template('courses.html', coursesList=coursesList)