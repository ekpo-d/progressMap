from flask import render_template, abort, redirect, url_for, request, flash
from flask_login import login_user,logout_user
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
			user = models.User.get_by_username(form.username.data)
			if user is not None and user.check_password(form.password.data):
				login_user(user, form.remember_me.data)
				flash('Login Successful.')
				return redirect (request.args.get('next') or url_for('user.userPage', username=user.username))
			flash('Incorrect username or password.')
			return redirect(url_for('main.show', page='login'))
		return render_template('login.html', form=form)
	elif page == 'signup':
		form = forms.SignupForm()
		if form.validate_on_submit():
			user = models.User(username=form.username.data, email=form.email.data, password=form.password.data)
			db.session.add(user)
			db.session.commit()
			flash('Thanks for signing up. Please log in.')
			return redirect(url_for('main.show', page='login'))
		return render_template('signup.html', form=form)
	elif page == 'signout':
		logout_user()
		return redirect(url_for('main.show', page='index'))
		
	else:
		abort(404)

@main.app_errorhandler(401)
def page_not_found(e):
	return render_template('401.html'), 401
		
@main.app_errorhandler(403)
def page_not_found(e):
	return render_template('403.html'), 403
	
@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500