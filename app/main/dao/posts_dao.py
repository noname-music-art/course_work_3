import json
from json import JSONDecodeError
from exceptions.data_exceptions import DataSourceError
from app.main.dao.post import Post


class PostsDAO:
    """DAO for posts"""

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """Load data from source"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Can`t get data from {self.path}')
        return data

    def _load_posts(self):
        """Load all posts as list[Post]"""
        post_data = self._load_data()
        list_of_posts: list[Post] = [Post(**post_data) for post_data in post_data]
        return list_of_posts

    def get_all(self):
        """Return list of posts"""
        posts = self._load_posts()
        return posts

    def get_by_pk(self, post_pk: int) -> Post:
        """Return Post by PK"""
        posts: list[Post] = self._load_posts()

        for post in posts:
            if post.pk == post_pk:
                return post
        raise ValueError('Такого поста не существует')

    def get_by_user(self, user_name: str) -> list[Post]:
        """Return list of posts by username"""
        posts = self._load_posts()
        posts_by_user: list[Post] = [post for post in posts if post.poster_name.lower() == user_name.lower()]
        if len(posts_by_user) > 0:
            return posts_by_user
        else:
            raise ValueError('Такого юзера нет')

    def search(self, query: str) -> list[Post]:
        """Return posts by query"""
        posts = self._load_posts()
        posts_by_query: list[Post] = [post for post in posts if query.lower() in post.content.lower()]
        if len(posts_by_query) >= 10:
            posts_by_query = posts_by_query[:10]
        return posts_by_query
