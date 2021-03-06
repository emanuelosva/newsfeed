"""User endpoints"""

from flask import Blueprint, request, jsonify
from uuid import uuid4
from typing import List
import app.users.auth as auth
from jwt.exceptions import InvalidSignatureError, DecodeError
from app.firebase.auth import controller as auth_controller
from app.firebase.firestore_service import add_news_site, delete_news_site

# Blueprint implementation
bp = Blueprint('users', __name__, url_prefix='/users')


# Response function
def make_response(error: bool, message: str, status: int, data={}):
    """
    Create a homogenized response
    Params:
    - error: bool, The status of error
    - message: str, A message to user for operation status
    - status: int, HTTP status code
    """
    res = jsonify({'error': error, 'message': message, 'data': data})
    return res, status


# ------------ Operations about user subscriptions --------- #

@bp.route('', methods=['POST', 'DELETE'])
def users_subscription():
    """
    Manage the user subscriptions

    POST: Add a new subscription to the user subscriptions list
    params:
    in: body
    - id: str, The user id
    - news_name: str, The new name identifier

    DELETE: Remove a subscription to the user subscriptions list
    params:
    in: body
    - id: str, The user id
    - news_name: str, The news name identifier  
    """

    try:
        # Authentication by jwt
        bearer = request.headers.get('Authorization')
        json_web_token = bearer.split(' ')[1]
        valid_token = auth.verify(json_web_token)
        # exist = db.find_user(valid_token.username)
        # if not exist:
        #     return make_response(error=True, message='Unauthorized', status=401)

        # Data from body
        body = request.get_json()
        user_id = body['email']
        news_name = body['news_name']

        if not (news_name == 'el_universal' or news_name == 'bbc' or news_name == 'new_york_times'):
            return make_response(error=True, message='Invalid news name', status=409)

        if request.method == 'POST':
            add_news_site(user_id, news_name)
            return make_response(error=False, message='Suscribed', status=201)
        else:
            exist_subscription = delete_news_site(user_id, news_name)
            if exist_subscription:
                message = f'The user is not subscribed to {news_name}'
                return make_response(error=True, message=message, status=409)
            return make_response(error=False, message='Unsuscribed', status=200)

    except (InvalidSignatureError, DecodeError, AttributeError):
        # If invalid jwt
        return make_response(error=True, message='Unauthorized', status=401)

    except (KeyError, TypeError):
        # If invalid body schema
        message = 'id and news_name are needed'
        return make_response(error=True, message=message, status=400)

    except Exception:
        # Return a 500 error if something went wrong
        return make_response(error=True, message='Server serror', status=500)


# ---------------- Operations about user --------------- #

@bp.route('/signup', methods=['POST'])
def signup():
    """
    Register a new user

    POST: Add a new user to db
    params:
    in: body
    - name: str, The user name
    - email: str, The user email
    - password: str, The user password
    """

    try:
        # Get data from body
        body = request.get_json()
        username = body['username']
        email = body['email']
        password = body['password']

        # Create the user
        existing_user = auth_controller.signup(username, email, password)
        if existing_user:
            return make_response(error=True, message='The user already exist', status=409)
        return make_response(error=False, message='User created', status=201)

    except (KeyError, TypeError):
        # If invalid body schema
        message = 'username, email and password are needed'
        return make_response(error=True, message=message, status=400)

    except Exception:
        # Return a 500 error if something went wrong
        return make_response(error=True, message='Server serror', status=500)


@bp.route('/login', methods=['POST'])
def login():
    """
    Login a user

    POST: Login user and send jwt cifred
    params:
    in: body
    - email: str, The user email
    - password: str, The user password
    """

    try:
        # Get data from body
        body = request.get_json()
        email = body['email']
        password = body['password']

        # Login the user and generate jwt
        user = auth_controller.login(email, password)
        if user is not None:
            # The credentials are correct
            token = auth.encode(user)
            data = {'token': token, 'user': user}
            return make_response(error=False, message='Logged', status=200, data=data)
        else:
            # The user does not exist or incorrect password
            return make_response(error=True, message='Unauthorized', status=401)

    except (KeyError, TypeError):
        # If invalid body schema
        message = 'email and password are needed'
        return make_response(error=True, message=message, status=400)

    except Exception:
        # Return a 500 error if something went wrong
        return make_response(error=True, message='Server Error', status=500)
