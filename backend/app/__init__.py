"""App factory"""

# Required imports
from flask import Flask


def create_app():
    """
    Return the flask app instance

    Params:
      - none
    Return:
      - app: The flask app instance
    """
    app = Flask(__name__)

    from .users import api as api_users
    from .news import api as api_news

    app.register_blueprint(api_users.bp)
    app.register_blueprint(api_news.bp)

    return app
