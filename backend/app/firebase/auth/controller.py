"""Autorization controller"""

# Password hash functions
from werkzeug.security import generate_password_hash, check_password_hash
# Firebase services
from app.firebase.firestore_service import user_add, get_user_by_email


def signup(username: str, email: str, password: str):
    """
    Register a new user in Firebase DB
    Paramas:
    - username: The username of user
    - email: The email user
    - password: The user password
    Return: none
    """
    # Get user data from db if exist
    user_validate = get_user_by_email(email)

    # User existing validation
    if user_validate.to_dict() is None:
        password_hash = generate_password_hash(password)
        user_data = {
            "username": username,
            "password_hash": password_hash,
            "email": email
        }
        user_add(user_data)
        return False
    else:
        error = 'El usuario ya existe, por favor valide la información'
        return True


def login(email: str, password: str):
    """
    Verify the user existence and user credentials
    Params:
    - email: user email
    - password: user password
    """
    # Verify is user existence
    user_validate = get_user_by_email(email)
    if user_validate.to_dict() is not None:

        # Compare password passed and password storage in db
        password_from_db = user_validate.to_dict()['password']
        check_password = check_password_hash(password_from_db, password)
        if check_password:
            user = user_validate.to_dict()
            # Remove data to no send it
            user['password'] = ''
            # If the user exist and correct password, retur data
            return user

        else:
            # The password is incorrect
            return None
    else:
        # The user does not exist
        return None
