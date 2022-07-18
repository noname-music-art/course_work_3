import json
from json import JSONDecodeError
from exceptions.data_exceptions import DataSourceError
from app.main.dao.comment import Comment


class CommentsDAO:
    """"""

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удаётся получить данные комментариев из {self.path}')
        return data

    def _load_comments(self):
        """"""
        comments_data = self._load_data()
        list_of_comments = [Comment(**comments_data) for comments_data in comments_data]
        return list_of_comments

    def get_by_post_pk(self, post_pk: int) -> list[Comment]:
        """"""
        comments = self._load_comments()
        comments_by_post_pk = [comment for comment in comments if comment.post_id == post_pk]
        return comments_by_post_pk
