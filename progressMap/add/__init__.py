from flask import Blueprint 

add = Blueprint('add', __name__)

from . import views