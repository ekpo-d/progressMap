from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = path.abspath(path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '\xcbP\x08\xf1\x9c\xe8\x9fq\x19\xf7\xf9\xb4\x05\xe3\xbc\x98A\x04\x9fw\xfa\t\x1cN'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'models.db')
db = SQLAlchemy(app)


from .main import main as main_blueprint
from .progress import progress as pr_blueprint
from .articles import articles as art_blueprint
from .post import post as post_blueprint
import models

app.register_blueprint(main_blueprint)
app.register_blueprint(pr_blueprint, url_prefix='/progress')
app.register_blueprint(art_blueprint, url_prefix='/articles')
app.register_blueprint(post_blueprint, url_prefix='/post')
