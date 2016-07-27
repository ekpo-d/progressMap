from flask import render_template, abort
from . import curriculums
from .. import models

@curriculums.route('/', defaults={'page': 'all'})
@curriculums.route('/<page>')
def show(page):
	if page == 'all':
		curriculumList = models.getFromDb(models.Curriculums, 6)
		return render_template('curriculums.html', curriculumList=curriculumList)
	elif page == models.getByTitle(models.Curriculums, page).title:
		curriculum = models.getByTitle(models.Curriculums, page)
		return render_template('showCurriculum.html', curriculum=curriculum)
	else:
		abort(404)
