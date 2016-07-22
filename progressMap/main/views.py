from flask import render_template, abort, redirect, url_for, request, flash
from flask_login import login_user
from .. import models, login_manager
from . import main, forms

@login_manager.user_loader
def load_user(userid):
	return models.User.query.get(int(userid))

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
			user = models.User.query.filter_by(username=form.username.data).first()
			if user is not None:
				login_user(user, form.remember_me.data)
				flash('Login Successful.')
				return redirect (request.args.get('next') or url_for('.show', page='map'))
			flash('Incorrect username or password.')
			return redirect(url_for('main.show', page='login'))
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