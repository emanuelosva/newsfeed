"""file of views of firebase integrations services"""
# #Blueprints
from . import auth
#flask
from flask import render_template, request, redirect, url_for
#Models
from .models import User, UserData
#firebase exceptions
from firebase_admin.auth import EmailAlreadyExistsError
#Forms
from .forms import SignupForms
#password hash
from werkzeug.security import generate_password_hash
#Firebase services
from .firestore_service import user_add

bp = auth.bp

@bp.route('signup/', methods=['POST', 'GET'])
def signup():
    """Logic for input and send data for create new user"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        password_hash = generate_password_hash(password)
        user_data = UserData(username, password_hash)
        user_add(user_data)


@bp.route('login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')