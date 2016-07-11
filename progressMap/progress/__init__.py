from flask import Blueprint

progress = Blueprint('progress', __name__)

from . import views
