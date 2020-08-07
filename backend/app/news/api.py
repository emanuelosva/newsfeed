"""News end poitn"""

# Required imports
from flask import Blueprint, request, jsonify
from app.users.api import make_response
from scrapy.scraping import get_news, news_providers

# Blueprint instance
bp = Blueprint('news', __name__, url_prefix='/news')


# ---------------- Operations about news --------------- #

@bp.route('', methods=['GET'])
def get_news_info():
    """
    Return the info acordly to the query news name provider
    GET:
    params:
    in: query
    - news_name: the news name identifier
    Return:
    - news_info: List[json], A array with the news info
    """

    try:
        # Get query
        news_name = request.args.get('news_name')
        if news_name:
            news_info = get_news(news_name)
            if not news_info:
                return make_response(error=True, message='Not Found', status=404)
            else:
                data = {
                    'info': news_info,
                    'copywrigt': f'The info and it rigths belogns to {news_providers[news_name]}'
                }
                return make_response(error=False, message='News Retrieved', status=200, data=data)
        else:
            raise KeyError

    except (TypeError, KeyError):
        # The query wasn't passed
        return make_response(error=True, message='news_name is needed in query', status=400)

    except Exception:
        # Return a 500 error if something went wrong
        return make_response(error=True, message='Server Error', status=500)
