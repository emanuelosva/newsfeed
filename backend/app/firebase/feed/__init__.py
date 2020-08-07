"""feed view logic"""

from flask import Blueprint

bp = Blueprint('feed', __name__, url_prefix='/')

from . import views



