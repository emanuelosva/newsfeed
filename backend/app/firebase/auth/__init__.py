"""init file of blueprint of firebase authentication system"""

from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

from . import views