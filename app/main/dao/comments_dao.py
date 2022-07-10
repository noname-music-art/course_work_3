import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        """ Загружаем комментарии"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_by_post_pk(self, post_pk: int) -> list[dict]:
        """ Возвращает комментарии к определенному посту"""
        comments = self.load_data()
        comments_by_post_pk = []
        for comment in comments:
            if comment["post_id"] == post_pk:
                comments_by_post_pk.append(comment)
        return comments_by_post_pk
