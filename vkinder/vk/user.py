"""
User модуль описывает свойства пользователя Вк для последующей обработки
"""


class User:
    """
    Defines user`s properties
    """
    def __init__(self, interests, books, movies, music, city):
        for param in [interests, books, movies, music]:
            if not isinstance(param, (list, tuple)):
                raise TypeError('Must be an iterable')
        if not isinstance(city, str):
            raise TypeError('city must be a string')
        self.interests = interests
        self.books = books
        self.movies = movies
        self.music = music
        self.city = city

