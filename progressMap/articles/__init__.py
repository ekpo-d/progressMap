from flask import Blueprint

articles = Blueprint('articles', __name__)

from . import views