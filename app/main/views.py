import logging

from flask import Blueprint, render_template, request, redirect
from app.main.dao.posts_dao import PostsDAO
from app.main.dao.comments_dao import CommentsDAO
from app.main.dao.bookmarks_dao import BookmarksDAO


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")
bookmarks_dao = BookmarksDAO("data/bookmarks.json")

logger = logging.getLogger("basic")


@main_blueprint.route('/')
def main():
    logger.debug("Были запрошены все посты")
    posts = posts_dao.get_all()
    bookmarks_count = len(bookmarks_dao.get_all_bookmarks())
    return render_template("index.html", posts=posts, bookmarks_count=bookmarks_count)


@main_blueprint.route('/posts/<int:post_pk>')
def post_page(post_pk):
    logger.debug(f"Был запрошен пост: {post_pk}")
    post = posts_dao.get_by_pk(post_pk)
    comments = comments_dao.get_by_post_pk(post_pk)
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


@main_blueprint.route('/bookmarks/')
def bookmarks_page():
    posts = bookmarks_dao.get_all_bookmarks()
    return render_template("bookmarks.html", posts=posts)


@main_blueprint.route('/bookmarks/add/<int:post_id>', methods=['POST'])
def add_bookmark(post_id):
    post = posts_dao.get_by_pk(post_id)
    bookmarks_dao.add_bookmark(post)
    return redirect("/", code=302)


@main_blueprint.route('/bookmarks/remove/<int:post_id>', methods=['POST'])
def delete_bookmark(post_id):
    bookmarks_dao.delete_bookmark(post_id)
    return redirect("/bookmarks/", code=302)
