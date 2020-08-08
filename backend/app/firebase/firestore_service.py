"""Firebase connection and functions"""

# Required imports
from firebase_admin import credentials, initialize_app, firestore
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

key = {
    "type": os.getenv('TYPE'),
    "project_id": os.getenv('PROJECT_ID'),
    "private_key_id": os.getenv('PRIVATE_KEY_ID'),
    "private_key": os.getenv('PRIVATE_KEY'),
    "client_email": os.getenv('CLIENT_EMAIL'),
    "client_id": os.getenv('CLIENT_ID'),
    "auth_uri": os.getenv('AUTH_URI'),
    "token_uri": os.getenv('TOKEN_URI'),
    "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL')
}

# Db connection
cred = credentials.Certificate(key)
default_app = initialize_app(cred)
db = firestore.client()


# ----------------------------- Db functions -------------------------#
def user_add(user_data):
    """
    Add new user to database
    Params:
    - user_data: dict, the user info
    Return: void
    """
    user = db.collection('users').document(user_data["email"])
    user.set({
        'username': user_data["username"],
        'password': user_data["password"],
        'news_sites': []
    })


def get_user_by_email(user_email):
    """
    Get user by id (id = email) from database
    Params:
    - user_email: str, The user email
    Return: void
    """
    return db.collection('users').document(user_email).get()


def add_news_site(user_id, news_name):
    """
    Add new subscription to user list
    Params:
    - user_id: The user email
    - news_name: The name of news provider
    Return: void
    """
    user_info = get_user_by_email(user_id)
    user_info = user_info.to_dict()
    list_news = user_info['news_sites']
    list_news.append(news_name)
    user_info['news_sites'] = list(set(list_news))
    db.collection('users').document(user_id).update(user_info)


def delete_news_site(user_id, news_name):
    """
    Delete subscription to user list
    Params:
    - user_id: The user email
    - news_name: The name of news provider
    Return: void
    """
    user_info = get_user_by_email(user_id)
    user_info = user_info.to_dict()
    list_news = user_info['news_sites']
    if list_news.count(news_name) != 0:
        list_news.remove(news_name)
    else:
        # The user is not subscribed to the currently passed news_name
        return True
    user_info['news_sites'] = list_news
    db.collection('users').document(user_id).update(user_info)
