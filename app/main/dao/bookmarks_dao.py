import json
from json import JSONDecodeError
from exceptions.data_exceptions import DataSourceError
from app.main.dao.bookmark import Bookmark


class BookmarksDAO:
    """DAO for Bookmarks"""

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
        """Load all marked posts as list[Bookmark]"""
        post_data = self._load_data()
        list_of_booked_posts = [Bookmark(**post_data) for post_data in post_data]
        return list_of_booked_posts

    def save_bookmark_to_json(self, bookmarks):
        """Save data"""
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False, indent=4, sort_keys=True)

    def get_all_bookmarks(self):
        """Return list of marked post"""
        booked_posts = self._load_posts()
        return booked_posts

    def add_bookmark(self, bookmark):
        """Mark post"""
        bookmarks = self.get_all_bookmarks()
        if all(bookmark.pk != mark.pk for mark in bookmarks):
            bookmarks.append(bookmark)
            self.save_bookmark_to_json([bookmark.__dict__ for bookmark in bookmarks])
        return bookmarks

    def delete_bookmark(self, post_id):
        """Unmark post"""
        bookmarks = self.get_all_bookmarks()
        for bookmark in bookmarks:
            if bookmark.pk == post_id:
                bookmarks.remove(bookmark)
                break
        self.save_bookmark_to_json([bookmark.__dict__ for bookmark in bookmarks])
