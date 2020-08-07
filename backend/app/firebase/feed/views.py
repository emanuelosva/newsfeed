
from . import feed

bp = feed.bp


@bp.route('/', methods=['POST', 'GET'])
@login_required
def feed():
    user_ip = session.get('user_ip')
    username = current_user.username
    news = request.form['news_site_name']
    favorites_sites = current_user.favorites_sites



        context = {
            'user_ip':user_ip,
            'username':username,

        }
    return render_template('feed.html')