"""Json web token auth funtions"""

# Required imports
import jwt
import os
from dotenv import load_dotenv


# Load env variables
load_dotenv()
SECRET = os.getenv('SECRET') or 'dev'


# ------------------------- JWT manage ----------------------#

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
