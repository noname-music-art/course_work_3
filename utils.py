import json


def load_posts_from_source():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def load_comments_from_source():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_all() -> list[dict]:
    return load_posts_from_source()


def get_posts_by_user(user_name):
    pass


def search_for_posts(query: str) -> list[dict]:
    """Search post by keyword"""
    result = []
    for post in load_posts_from_source():
        if query.lower() in post['content'].lower():
            result.append(post)
    return result


def get_post_by_pk(post_pk: int) -> dict:
    for post in get_posts_all():
        if post['pk'] == post_pk:
            return post


def get_comments_by_post_id(post_pk: int) -> list[dict]:
    result = []
    for comment in load_comments_from_source():
        if comment['post_id'] == post_pk:
            result.append(comment)
    return result
