"""Its file for integrate services of firebase"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage

storage_client = storage.Client()
default_app = firebase_admin.initialize_app()

db = firestore.client()

def user_add(user_data):
    user = db.collection('users').document(user_data.username)
    user.set({'password':user_data.password})