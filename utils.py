import json


def get_posts_all() -> list[dict]:
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    pass


def get_comments_by_post_id(post_id):
    pass


def search_for_posts(query):
    pass


def get_post_by_pk(pk):
    pass
