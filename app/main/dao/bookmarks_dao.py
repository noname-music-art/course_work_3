import json
from json import JSONDecodeError
from exceptions.data_exceptions import DataSourceError
from app.main.dao.bookmark import Bookmark


class BookmarksDAO:
    """"""

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удаётся получить данные постов из {self.path}')
        return data

    def _load_posts(self):
        """"""
        post_data = self._load_data()
        list_of_booked_posts = [Bookmark(**post_data) for post_data in post_data]
        return list_of_booked_posts

    def save_bookmark_to_json(self, bookmarks):
        """"""
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False)

    def get_all_bookmarks(self):
        """"""
        booked_posts = self._load_posts()
        return booked_posts

    def add_bookmark(self, bookmark):
        """"""
        bookmarks = self.get_all_bookmarks()
        if bookmark not in bookmarks:
            bookmarks.append(bookmark)
            self.save_bookmark_to_json(bookmarks)

        return bookmarks

    def delete_bookmark(self, post_id):
        """"""
        bookmarks = self.get_all_bookmarks()
        for index, bookmark in enumerate(bookmarks):
            if bookmark['pk'] == post_id:
                del bookmarks[index]
                break
        self.save_bookmark_to_json(bookmarks)
