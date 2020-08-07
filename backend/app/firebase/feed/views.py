"""News feed view"""

#blueprint
from . import bp
#flask
from flask import render_template, redirect, request, session, url_for, flash
from flask_login import login_required, current_user
#firestore service
from app.firebase.firestore_service import add_news_site, delete_news_site


@bp.route('feed/', methods=['POST', 'GET'])
@login_required
def feed():
    email = current_user.id
    if request.method == 'POST':
        if request.form == request.form['add_new']:
            return redirect(url_for('feed'))

    return render_template('feed.html')


@bp.route('feed/add_news_site', methods=['POST'])
def add_news():
    if request.method == 'POST':
        email = current_user.id
        news_site_name = request.form['news_site_name']
        add_news_site(email, news_site_name)
        flash(f'Se ha agregado {news_site_name} a su lista de favoritos')
    return redirect(url_for('feed'))


@bp.route('feed/delete_news_site', methods=['POST'])
def delete_news():
    if request.method == 'POST':
        email = current_user.id
        news_site_name = request.form['news_site_name']
        delete_news_site(email, news_site_name)
    return redirect(url_for('feed'))