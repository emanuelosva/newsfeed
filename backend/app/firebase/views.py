"""file of views of firebase integrations services"""
# #Blueprints
from . import auth
#flask
from flask import render_template, request, redirect, url_for

#Models
from .models import User

#firebase exceptions
from firebase_admin.auth import EmailAlreadyExistsError

bp = auth.bp

@bp.route('signup/', methods=('POST'))
def signup():
    """Logic for input and send data for create new user"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        passwd_confirm = request.POST['password_confirmation']
        try:
            user = User(username, email, password)
            user.create_user()
            return redirect(url_for('login'))
        except EmailAlreadyExistsError:
            error = 'El usuario ya está registrado, por favor verifique sus datos'
            return render_template('signup.html', error=error)

    return render_template('signup.html')


@auth.route('login', methods=('POST'))
def login():
    pass