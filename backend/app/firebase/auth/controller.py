"""file of autoristion controller"""
# flask
from flask import request
# password hash
from werkzeug.security import generate_password_hash, check_password_hash
# Firebase services
from app.firebase.firestore_service import user_add, get_user_by_email


def signup(username: str, email: str, password: str):
    """
    Register a new user
    Params:
    - username: str, The user username
    - email: str, The email user
    - password: str, The user password
    Return: Boolean
    - True: The user register was correctly
    - Flase: The user already exist
    """

    user_validate = get_user_by_email(email)
    if user_validate.to_dict() is None:
        password_hash = generate_password_hash(password)
        user_data = {
            "username": username,
            "password": password_hash,
            "email": email
        }
        user_add(user_data)
        return False
    else:
        # The user already exists
        return True


def login(email: str, password: str):
    """
    Verify the user credentials and retur the user info if it are
    Params:
    - email: str, The user email
    - password: str, The user password
    Return:
    - Valid credentials: dict, The user info
    - Invalid credentials: None
    """

    user_validate = get_user_by_email(email)
    if user_validate.to_dict() is not None:
        password_from_db = user_validate.to_dict()['password']
        check_password = check_password_hash(password_from_db, password)
        if check_password:
            # Valid credentials
            user = user_validate.to_dict()
            user['password'] = ''
            return user

        else:
            # Invalid credentials
            return None
    else:
        # Invalid credentials
        return None
