import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object(os.getenv('FLASK_CONFIGURATION', 'progressMap.settings.DevelopmentConfig'))
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.show'
login_manager.init_app(app)

from .main import main as main_blueprint
from .add import add as add_blueprint
from .articles import articles as articles_blueprint
from .courses import courses as courses_blueprint
from .curriculums import curriculums as curriculums_blueprint
from .questions import questions as questions_blueprint
from .user import user as user_blueprint

import models

app.register_blueprint(main_blueprint)
app.register_blueprint(add_blueprint, url_prefix='/add')
app.register_blueprint(articles_blueprint, url_prefix='/articles')
app.register_blueprint(courses_blueprint, url_prefix='/courses')
app.register_blueprint(curriculums_blueprint, url_prefix='/curriculums')
app.register_blueprint(questions_blueprint, url_prefix='/questions')
app.register_blueprint(user_blueprint, url_prefix='/user')

