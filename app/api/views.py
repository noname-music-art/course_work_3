import logging

from flask import Blueprint, jsonify

from app.main.dao.post import Post
from app.main.dao.posts_dao import PostsDAO

api_blueprint = Blueprint("api_blueprint", __name__)

posts_dao = PostsDAO("data/posts.json")

logger = logging.getLogger("basic")


@api_blueprint.route('/api/posts/', methods=['GET'])
def api_get_posts_all():
    logger.info('Get all posts by API')
    posts: list[Post] = posts_dao.get_all()
    return jsonify([post.__dict__ for post in posts])


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def api_get_post_by_id(post_id: int):
    logger.info(f'post {post_id}')
    post: Post = posts_dao.get_by_pk(post_id)
    return jsonify(post.__dict__)

