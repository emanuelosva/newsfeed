from flask import Blueprint, request, jsonify, Response
from uuid import uuid4

bp = Blueprint('users', __name__, url_prefix='/users')

def make_response(error: bool, message: str, status: int):
    res = jsonify({ 'error': error, 'message': message })
    return res, status


@bp.route('', methods=['POST', 'DELETE'])
def users_subscription():
    body = request.get_json()
    try:
        user_id = body['id']
        news_id = body['news_id']
    except (KeyError, TypeError):
        message = 'id and news_id are needed'
        return make_response(error=True, message=message, status=400)

    try:
        if request.method == 'POST':
            # result = db.add_new_to_user(user_id, news_id)
            return make_response(error=False, message='Suscribed', status=201)
        else:
            # result = db.remove_new_to_user(user_id, news_id)
            return make_response(error=False, message='Unsuscribed', status=200)
    except e:
        return make_response(error=True, message='Server serror', status=500)
