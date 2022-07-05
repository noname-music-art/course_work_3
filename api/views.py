from flask import Blueprint, jsonify
from utils import load_posts_from_source, get_post_by_pk, get_posts_all


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts', methods=['GET'])
def get_posts_all():
    posts: list[dict] = load_posts_from_source()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id: int):
    post: dict = get_post_by_pk(post_id)
    return jsonify(post)
