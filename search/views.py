from flask import Blueprint, render_template, request
from utils import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    posts = search_for_posts(search_query)
    return render_template('search.html', query=search_query, posts=posts)
