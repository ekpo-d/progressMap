from flask import Blueprint 

questions = Blueprint('questions', __name__)

from . import views