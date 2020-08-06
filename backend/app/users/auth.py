"""Json web token auth funtions"""

import jwt

SECRET = 'secret_dev'

def encode(payload):
    """
    Encode the jwt
    Params:
    - payload: the user info
    Return:
    - encoded: the encoded jwt
    """
    encoded = jwt.encode(payload, SECRET, algorithm='HS256')
    return encoded.decode()

def verify(token):
    """
    Verify the jwt
    Params:
    - token: the encoded json web token
    Return:
    - valid_token: the payload decoded if the token is valid
    """
    valid_token = jwt.decode(token, SECRET, algorithm='HS256')
    return valid_token
