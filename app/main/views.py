import logging

from flask import Blueprint, render_template, request, abort
from app.main.dao.posts_dao import PostsDAO
from app.main.dao.comments_dao import CommentsDAO


posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")


@posts_blueprint.route('/')
def posts_all():
    logger.debug("Были запрошены все посты")
    posts = posts_dao.get_all()
    return render_template("index.html", posts=posts)


@posts_blueprint.route('/posts/<post_pk>')
def post_page(post_pk):
    logger.debug(f"Был запрошен пост: {post_pk}")
    post = posts_dao.get_by_pk(post_pk)
    comments = comments_dao.get_by_post_pk(post_pk)
    number_of_comments = len(comments)
    return render_template("post.html", post=post, comments=comments, number_of_comments=number_of_comments)


@posts_blueprint.route('/search/')
def posts_search():
    query = request.args.get("s", "")

    if query != "":
        posts = posts_dao.search(query)
        number_of_posts = len(posts)
    else:
        posts = []
        number_of_posts = 0

    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)


@posts_blueprint.route('/user_feed/<poster_name>')
def posts_by_user(poster_name):
    posts = posts_dao.get_by_user(poster_name)
    number_of_posts = len(posts)
    return render_template("user_feed.html", posts=posts, number_of_posts=number_of_posts)