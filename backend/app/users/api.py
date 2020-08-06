from flask import Blueprint, request, jsonify
from uuid import uuid4

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])
def signup():
    return jsonify({'hello': 'news'})
