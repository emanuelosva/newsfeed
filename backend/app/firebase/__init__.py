"""init file of blueprint of firebase authentication system"""

#flask
from flask import Blueprint

# firebase authentication system blueprint
fb_auth = Blueprint('fb_auth', __name__, url_prefix='/fb_auth')
