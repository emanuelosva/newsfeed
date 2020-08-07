"""file of views of firebase integrations services"""
# #Blueprints
from . import auth, feed
#flask
from flask import render_template, request, redirect, url_for, flash, make_response, session
from flask_login import login_required, login_user, logout_user
#Models
from .models import UserData, UserModel
#firebase exceptions
from firebase_admin.auth import EmailAlreadyExistsError
#Forms
from .forms import SignupForms
#password hash
from werkzeug.security import generate_password_hash, check_password_hash
#Firebase services
from .firestore_service import user_add, get_user_by_email

bp = auth.bp
feed = feed.feed

@bp.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/feed'))
    session['user_ip'] = user_ip

    return response

@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    """Logic for input and send data for create new user"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user_validate = get_user_by_email(email)
        if user_validate.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash, email)
            user_add(user_data)
            return redirect(url_for('auth.login'))
        else:
            error = 'El usuario ya existe, por favor valide la información'
            return render_template('signup.html', error=error)
    
    return render_template('signup.html')


@bp.route('login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user_validate = get_user_by_email(email)
        if user_validate.to_dict() is not None:
            password_from_db = user_validate.to_dict()['password']
            check_password = check_password_hash(password_from_db, password)
            if check_password:
                username = user_validate.to_dict()['username']
                user_data = UserData(username, password, email)
                user = UserModel(user_data)

                login_user(user)

                return redirect(url_for('feed'))
            else:
                error = 'Contraseña o nombre de usuario incorrectos'
                return render_template('login.html', error=error)
        else:
            flash('El usuario no existe, verifique su correo')

    return render_template('login.html')



@feed.route('/', methods=['POST', 'GET'])
@login_required
def feed():
    if request.method == 'POST':
        user_ip = session.get('user_ip')
        username = current_user.id

        context = {
            'user_ip':user_ip,
        }
    return render_template('feed.html')


@bp.route('/logout/')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('auth.login'))