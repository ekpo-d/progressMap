from flask import render_template
from . import courses
from .. import models

@courses.route('/', defaults={'page':'all'})
@courses.route('/<page>')
def show(page):
	if page == 'all':
		coursesList = models.getFromDb(models.Courses, 6)
		return render_template('courses.html', coursesList=coursesList)
	elif page == models.getByTitle(models.Courses, page).title:
		course = models.getByTitle(models.Courses, page)
		return render_template('showCourse.html', course=course)
	else:
		abort(404)