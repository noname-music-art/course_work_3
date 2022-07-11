import logging

from flask import Blueprint, render_template, request
from app.main.dao.posts_dao import PostsDAO
from app.main.dao.comments_dao import CommentsDAO


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")


@main_blueprint.route('/')
def main():
    logger.debug("Были запрошены все посты")
    posts: list[dict] = posts_dao.get_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route('/posts/<int:post_pk>')
def post_page(post_pk):
    logger.debug(f"Был запрошен пост: {post_pk}")
    post: dict = posts_dao.get_by_pk(post_pk)
    comments: list[dict] = comments_dao.get_by_post_pk(post_pk)
    return render_template("post.html", post=post, comments=comments)


@main_blueprint.route('/search/')
def posts_search():
    query = request.args.get("s", "")
    if query == "":
        posts = []
        number_of_posts = 0
    else:
        posts = posts_dao.search(query)
        number_of_posts = len(posts)
    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)


@main_blueprint.route('/user_feed/<poster_name>')
def posts_by_user(poster_name):
    posts = posts_dao.get_by_user(poster_name)
    return render_template("user_feed.html", posts=posts)
