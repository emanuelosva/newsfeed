"""Its file for integrate services of firebase"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage

storage_client = storage.Client()
default_app = firebase_admin.initialize_app()

db = firestore.client()

def user_add(user_data):
    """Add new user to database"""
    user = db.collection('users').document(user_data.email)
    user.set({
        'username':user_data.username,
        'password':user_data.password,
    })


def get_user_by_email(user_email):
    """get user by UID from database"""
    return db.collection('users').document(user_email).get()