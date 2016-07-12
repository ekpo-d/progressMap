from flask import Flask
from .main import main as main_blueprint
from .progress import progress as pr_blueprint
from .articles import articles as art_blueprint
from .post import post as post_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(pr_blueprint, url_prefix='/progress')
app.register_blueprint(art_blueprint, url_prefix='/articles')
app.register_blueprint(post_blueprint, url_prefix='/post')
