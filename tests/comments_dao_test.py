import pytest

from app.main.dao.comment import Comment
from app.main.dao.comments_dao import CommentsDAO


def check_fields(comment):

    fields = ["post_id", "commenter_name", "comment", "pk"]

    for field in fields:
        assert hasattr(comment, field), f"Нет поля {field}"


class TestCommentsDAO:

    @pytest.fixture
    def post_dao(self):
        comment_dao_instance = CommentsDAO("../tests/comments_mock.json")
        return comment_dao_instance

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
        assert pks == correct_pks, "Не совпадает id"

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, "Incorrect type for single post"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_by_pk(999)
        assert post is None, "Should be None for none existent pk"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_ids(self, post_dao, pk):
        post = post_dao.get_by_pk(pk)
        assert post.pk == pk, f"Incorrect PK for post with pk = {pk}"
