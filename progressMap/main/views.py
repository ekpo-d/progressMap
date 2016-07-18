from flask import render_template, abort, redirect, url_for
from .. import models
from . import main, forms

User = models.User()

@main.route('/', defaults={'page' : 'index'})
@main.route('/<page>', methods=['GET', 'POST'])
def show(page):
	if page == 'index':
		return render_template('index.html')
	elif page == 'map':
		return render_template('map.html')
	elif page == 'login':
		form = forms.LoginForm()
		if form.validate_on_submit():
			user = User.query.filter_by(username=form.username.data).first()
			if user is not None:
				return redirect (url_for('.show', page='map'))
		return render_template('login.html', form=form)
	elif page == 'signup':
		return render_template('signup.html')
	else:
		abort(404)

	
@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500