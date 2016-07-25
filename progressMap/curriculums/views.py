from flask import render_template
from . import curriculums
from .. import models

@curriculums.route('/')
def show():
	curriculumList = models.getFromDb(models.Curriculums, 6)
	return render_template('curriculums.html', curriculumList=curriculumList)