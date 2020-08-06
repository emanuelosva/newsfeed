from flask import Blueprint, request, jsonify, Response
from uuid import uuid4
from typing import List
import app.users.auth as auth
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
    - news_id: str, The new id identifier
    
    DELETE: Remove a subscription to the user subscriptions list
    params:
    in: body
    - id: str, The user id
    - news_name: str, The news name identifier  
    """
    # Verify token and check authentication
    try:
        bearer = request.headers.get('Authorization')
        json_web_token = bearer.split(' ')[1]
        valid_token = auth.verify(json_web_token)
    except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.DecodeError):
        return make_response(error=True, message='Unauthorized', status=401)

    # Make sure the body has the correct schema
    body = request.get_json()
    try:
        user_id = body['id']
        news_name = body['news_name']
    except (KeyError, TypeError):
        message = 'id and news_name are needed'
        return make_response(error=True, message=message, status=400)

    # Make the operation acording to the method
    try:
        if request.method == 'POST':
            # result = db.add_new_to_user(user_id, news_name)
            return make_response(error=False, message='Suscribed', status=201)
        else:
            # result = db.remove_new_to_user(user_id, news_name)
            return make_response(error=False, message='Unsuscribed', status=200)
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

    # Make sure the body has the correct schema
    body = request.get_json()
    try:
        name = body['name']
        email = body['email']
        password = body['password']
    except (KeyError, TypeError):
        message = 'name, email and password are needed'
        return make_response(error=True, message=message, status=400)

    # Create the user
    try:
        # result = db.create_user(name, email, password)
        return make_response(error=False, message='User created', status=201)
    except e:
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

    # Make sure the body has the correct schema
    body = request.get_json()
    try:
        email = body['email']
        password = body['password']
    except (KeyError, TypeError):
        message = 'email and password are needed'
        return make_response(error=True, message=message, status=400)

    # Login the user and generate jwt
    try:
        # user = db.login(mail, password)
        user = { 'name': 'Test', 'subscriptions': ['el_universal', 'excelsior'] }
        if user is not None:
            token = auth.encode(user)
            data= { 'token': token, 'user': user}
            return make_response(error=False, message='Logged', status=200, data=data)
        else:
            return make_response(error=True, message='Unauthorized', status=401)

    except Exception:
        return make_response(error=True, message='Server Error', status=500)
