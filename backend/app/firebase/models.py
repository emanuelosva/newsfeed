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

    def create_user(self):
        firebase_admin.auth.create_user(
            display_name = self.username,
            email = self.email, 
            password= self.password,
            email_verified = False 
        )


class UserData():
    def __init__(self, username, password):
        self.username = username
        self.password = password