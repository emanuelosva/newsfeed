"""file of views of firebase integrations services"""
#Blueprints
from . import fb_auth
#flask
from flask import render_template

@fb_auth('/signup', methods=('POST'))
def signup():
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwd_confirm = request.POST['password_confirmation']
    
    return render_template('signup.html')