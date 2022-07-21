import pytest

from run import app


class TestApi:

    @pytest.fixture
    def app_instance(self):
        test_client = app.test_client()
        return test_client

    def test_all_posts(self, app_instance):
        result = app_instance.get("/api/posts/")
        assert result.status_code == 200
        assert result.mimetype == "application/json"

    def test_one_post(self, app_instance):
        result = app_instance.get("/api/posts/1")
        assert result.status_code == 200
        assert result.mimetype == "application/json"
