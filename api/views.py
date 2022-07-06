import logging.config

from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts', methods=['GET'])
def api_get_posts_all():
    logger.info('Get all posts by API')
    posts: list[dict] = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def api_get_post_by_id(post_id: int):
    logger.info(f'post {post_id}')
    post: dict = get_post_by_pk(post_id)
    return jsonify(post)