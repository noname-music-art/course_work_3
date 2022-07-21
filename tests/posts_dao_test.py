import pytest

from app.main.dao.post import Post
from app.main.dao.posts_dao import PostsDAO


def check_fields(post):

    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    for field in fields:
        assert hasattr(post, field), f"Нет поля {field}"


class TestPostsDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostsDAO("../tests/posts_mock.json")
        return post_dao_instance

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, "Incorrect type"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "Incorrect type"

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_all()
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_all()
        correct_pks = {1, 2, 3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, "Post ID not correct"

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, "Incorrect type for single post"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_by_pk(1)
        check_fields(post)

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_ids(self, post_dao, pk):
        post = post_dao.get_by_pk(pk)
        assert post.pk == pk, f"Incorrect PK for post with pk = {pk}"
