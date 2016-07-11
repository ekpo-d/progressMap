from flask import Flask
from .main import main as main_blueprint
from .progress import progress as pr_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(pr_blueprint, url_prefix='/progress')

