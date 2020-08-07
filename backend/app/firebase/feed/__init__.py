"""feed view logic"""

from flask import Blueprint

bp = ('feed', __name__, url_prefix='/')

from . import views



