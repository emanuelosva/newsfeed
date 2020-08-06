"""File of users models"""
#Firebase services
import firebase_admin
from firebase_admin import auth
from google.cloud import storage

storage_client = storage.Client()
default_app = firebase_admin.initialize_app()

class User():
    """Logic for create and authenticate users"""

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    