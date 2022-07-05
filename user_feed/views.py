from flask import Blueprint, render_template
from utils import get_posts_by_user

user_feed_blueprint = Blueprint('user_feed', __name__, template_folder='templates')


@user_feed_blueprint.route('/user_feed/<poster_name>')
def user_feed_page(poster_name):
    posts: list[dict] = get_posts_by_user(poster_name)
    return render_template('user_feed.html', posts=posts)
