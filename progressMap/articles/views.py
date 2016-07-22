from flask import render_template
from . import articles
from .. import models

@articles.route('/')
def show():
	articlesList = models.getFromDb(models.Articles, 6)
	return render_template('articles.html', articlesList=articlesList)