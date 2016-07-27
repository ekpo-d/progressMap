from flask import render_template
from . import articles
from .. import models

@articles.route('/', defaults={'page':'all'})
@articles.route('/<page>')
def show(page):
	if page == 'all':
		articlesList = models.getFromDb(models.Articles, 6)
		return render_template('articles.html', articlesList=articlesList)
	elif page == models.getByTitle(models.Articles, page).title:
		course = models.getByTitle(models.Articles, page)
		return render_template('showArticle.html', article=article)
	else:
		abort(404)