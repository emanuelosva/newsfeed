"""App factory"""

# Required imports
from flask import Flask
from flask_login import LoginManager
from .config import Config
from .firebase.models import UserModel

login_manager=LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(email):
  return UserModel.query(email)


def create_app():
    """
    Return the flask app instance

    Params:
      - none
    Return:
      - app: The flask app instance
    """
    app = Flask(__name__)

    login_manager.init_app(app)

    app.config.from_object(Config)

    from .users import api
    app.register_blueprint(api.bp)

    from .firebase import auth
    app.register_blueprint(auth.bp)

    from .firebase import feed
    app.register_blueprint(feed.bp)

    return app
