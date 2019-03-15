"""
Mодуль описывает свойства пользователя Вк для последующей обработки
"""

from typing import List
from vkinder.evaluators import eval_city, eval_interests, eval_movies, eval_books, eval_music
from vkinder.field_adapters import city_to_string, split_string


EVALUATORS = {
    'city': eval_city,
    'interests': eval_interests,
    'music': eval_music,
    'books': eval_books,
    'movies': eval_movies,
}

ADAPTERS = {
    'city': city_to_string,
    'interests': split_string,
    'music': split_string,
    'books': split_string,
    'movies': split_string,

}


class BaseField:

    mytype = str

    def __init__(self, name, value, weight=1):
        self.check_type_name(name)
        self.check_type_value(value)
        self.check_type_weight(weight)

        self.name = name
        self.value = value
        self.weight = weight

    def adapters_name(self, city):
        if self.name == 'city':
            return city['title']


    @staticmethod
    def check_type_name(name):
        """
        Name is always string. Check if string only
        """
        if isinstance(name, str):
            return name
        raise TypeError('name must be an instance of string')

    @staticmethod
    def check_type_weight(weight):
        if isinstance(weight, int):
            return weight
        raise TypeError('Weight must be an integer')

    def check_type_value(self, value):
        if isinstance(value, self.mytype):
            return value
        raise TypeError('value must be an instance of %s' % type(self.mytype))


class StringField(BaseField):
    mytype = str


class ListField(BaseField):
    mytype = list


class SearchParams:
    def __init__(self, fields: List[BaseField]) -> None:
        self.registry = dict()
        for field in fields:
            self.registry[field.name] = field

