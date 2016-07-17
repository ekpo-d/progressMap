from flask import Blueprint

curriculums = Blueprint('curriculums', __name__)

from . import views