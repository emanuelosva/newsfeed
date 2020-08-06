from flask import Blueprint, request, jsonify, Response
from uuid import uuid4

# Blueprint implementation
bp = Blueprint('users', __name__, url_prefix='/users')

# Useful funtion
def make_response(error: bool, message: str, status: int):
    """
    Create a homogenized response
    Params:
    - error: bool, The status of error
    - message: str, A message to user for operation status
    - status: int, HTTP status code
    """
    res = jsonify({ 'error': error, 'message': message })
    return res, status


# ------------ Operations about user subscriptions --------- #

@bp.route('', methods=['POST', 'DELETE'])
def users_subscription():
    """
    Manage the user subscriptions

    Allowed methods:
    - POST:
        Add a new subscription to the user subscriptions list
        params:
        in: body
        - id: str, The user id
        - news_id: str, The new id identifier
    - POST:
        Add a new subscription to the user subscriptions list
        params:
        in: body
        - id: str, The user id
        - news_id: str, The new id identifier  
    """

    body = request.get_json()

    # Make sure the body has the correct schema
    try:
        user_id = body['id']
        news_id = body['news_id']
    except (KeyError, TypeError):
        message = 'id and news_id are needed'
        return make_response(error=True, message=message, status=400)

    # Make the operation acording to the method
    try:
        if request.method == 'POST':
            # result = db.add_new_to_user(user_id, news_id)
            return make_response(error=False, message='Suscribed', status=201)
        else:
            # result = db.remove_new_to_user(user_id, news_id)
            return make_response(error=False, message='Unsuscribed', status=200)
    except e:
        # Return a 500 error if something went wrong
        return make_response(error=True, message='Server serror', status=500)
