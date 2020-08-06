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

    from .users import api
    app.register_blueprint(api.bp)

    return app
