from flask import Blueprint, request, jsonify, Response
from uuid import uuid4
from typing import List
import app.users.auth as auth
from jwt.exceptions import InvalidSignatureError, DecodeError
import jwt

# Blueprint implementation
bp = Blueprint('users', __name__, url_prefix='/users')

# Useful funtion
def make_response(error: bool, message: str, status: int, data={}):
    """
    Create a homogenized response
    Params:
    - error: bool, The status of error
    - message: str, A message to user for operation status
    - status: int, HTTP status code
    """
    res = jsonify({ 'error': error, 'message': message, 'data': data })
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
    # Verify token and check authentication
    try:
        # Authentication by jwt
        bearer = request.headers.get('Authorization')
        json_web_token = bearer.split(' ')[1]
        valid_token = auth.verify(json_web_token)

        # Data from
        body = request.get_json()
        user_id = body['id']
        news_name = body['news_name']

        if request.method == 'POST':
            # result = db.add_new_to_user(user_id, news_name)
            return make_response(error=False, message='Suscribed', status=201)
        else:
            # result = db.remove_new_to_user(user_id, news_name)
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
        name = body['name']
        email = body['email']
        password = body['password']

        # Create the user
        id = uuid4()
        # result = db.create_user(id, name, email, password)
        return make_response(error=False, message='User created', status=201)

    except (KeyError, TypeError):
        # If invalid body schema
        message = 'name, email and password are needed'
        return make_response(error=True, message=message, status=400)

    except Exception:
        # Return a 500 error if something went wrong
        return make_response(error=True, message='Server serror', status=500)


@bp.route('/login', methods=['POST'])
def login():
    """
    Login a user

    POST: Login user and sed jwt cifred
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
        # user = db.login(mail, password)
        user = { 'name': 'Stan', 'subscriptions': ['el_universal', 'excelsior'] }
        if user is not None:
            # The credentials are correct
            token = auth.encode(user)
            data= { 'token': token, 'user': user}
            return make_response(error=False, message='Logged', status=200, data=data)
        else:
            # The user does not exist or icorrect password
            return make_response(error=True, message='Unauthorized', status=401)

    except (KeyError, TypeError):
        # If invalid body schema
        message = 'email and password are needed'
        return make_response(error=True, message=message, status=400)

    except Exception:
        # Return a 500 error if something went wrong
        return make_response(error=True, message='Server Error', status=500)
