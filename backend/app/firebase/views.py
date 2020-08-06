"""file of views of firebase integrations services"""
# #Blueprints
from . import auth
#flask
from flask import render_template, request

#Models
from .models import User

bp = auth.bp

@bp.route('signup/', methods=('POST', 'GET'))
def signup():
    """Logic for input and send data for create new user"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # passwd_confirm = request.POST['password_confirmation']
    
        user = User(username, email, password)
        user.create_user()
        return render_template('signup.html')

    return render_template('signup.html')