"""News feed view"""

#flask
from flask import render_template, redirect, request, session, url_for
from flask_login import login_required, current_user
#blueprint
from . import bp


@bp.route('feed/', methods=['POST', 'GET'])
@login_required
def feed():
    return render_template('feed.html')

@bp.route('', methods=['POST'])
def add_news():
    user_id = current_user.username

    return redirect(url_for('feed'))
    