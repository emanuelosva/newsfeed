"""file of views of firebase integrations services"""
# #Blueprints
from . import auth
#flask
from flask import render_template, request, redirect, url_for, flash
#Models
from .models import UserData
#firebase exceptions
from firebase_admin.auth import EmailAlreadyExistsError
#Forms
from .forms import SignupForms
#password hash
from werkzeug.security import generate_password_hash
#Firebase services
from .firestore_service import user_add, get_user

bp = auth.bp

@bp.route('signup/', methods=['POST', 'GET'])
def signup():
    """Logic for input and send data for create new user"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user_validate = get_user(username)
        if user_validate.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash, email)
            user_add(user_data)
            return redirect(url_for('auth.login'))
        else:
            flash('El usuario ya existe. \n Por favor valide la información')
    
    return render_template('signup.html')


@bp.route('login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')