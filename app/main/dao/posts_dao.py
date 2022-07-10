import json


class PostsDAO:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        """ Возвращает список со всеми данными"""
        candidates = self.load_data()
        return candidates

    def get_by_pk(self, post_pk: int) -> dict:
        """ Возвращает один пост по его номеру"""
        posts = self.load_data()
        for post in posts:
            if post["pk"] == post_pk:
                return post

    def get_by_user(self, user_name):
        """ Возвращает посты указанного пользователя"""
        posts = self.get_all()
        posts_by_user = []
        for post in posts:
            if post["poster_name"] == user_name:
                posts_by_user.append(post)
        return posts_by_user

    def search(self, query: str) -> list[dict]:
        """ Возвращает список словарей по вхождению query"""
        posts = self.get_all()
        posts_by_query = []
        for post in posts:
            if query.lower() in post["content"].lower():
                posts_by_query.append(post)
                if len(posts_by_query) >= 10:
                    posts_by_query = posts_by_query[:10]
        return posts_by_query
