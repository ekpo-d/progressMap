from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from . import forms, main
from .. import login_manager, models


@login_manager.user_loader
def load_user(userid):
    return models.User.query.get(int(userid))


def login_function():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = form.login_user()
        if user:
            flash('Login Successful.')
            return redirect(request.args.get('next') or url_for('user.userPage', username=user.username))
        flash('Incorrect username or password.')
        return redirect(url_for('main.show', page='login'))
    return render_template('login.html', form=form)


def signup_function():
    form = forms.SignupForm()
    if form.validate_on_submit():
        form.save()
        flash('Thanks for signing up. Please log in.')
        return redirect(url_for('main.show', page='login'))
    return render_template('signup.html', form=form)


def signout_function():
    logout_user()
    return redirect(url_for('main.show', page='index'))


@main.route('/', defaults={'page': 'index'})
@main.route('/<page>', methods=['GET', 'POST'])
def show(page):
    options = {
        'index': lambda: render_template('pages/index.html'),
        'map': lambda: render_template('map.html'),
        'login': login_function,
        'signup': signup_function,
        'signout': signout_function,
    }
    try:
        return options[page]()
    except KeyError:
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
