"""file of autoristion controller"""
#flask
from flask import request 
#password hash
from werkzeug.security import generate_password_hash, check_password_hash
#Firebase services
from app.firebase.firestore_service import user_add, get_user_by_email


def signup(username, email, password):
    """Logic for input and send data for create new user"""

    user_validate = get_user_by_email(email)
    if user_validate.to_dict() is None:
        password_hash = generate_password_hash(password)
        user_data = UserData(username, password_hash, email)
        user_add(user_data)
        return False
    else:
        error = 'El usuario ya existe, por favor valide la información'
        return True


def login(email, password):
    user_validate = get_user_by_email(email)
    if user_validate.to_dict() is not None:
        password_from_db = user_validate.to_dict()['password']
        check_password = check_password_hash(password_from_db, password)
        if check_password:
            user = user_validate.to_dict()
            user['password'] = ''
            return user

        else:
            return None
    else:
        return None

