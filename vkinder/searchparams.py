"""
User модуль описывает свойства пользователя Вк для последующей обработки
"""

# An idea: use classes (like Field) as an input for User`s constuctor:
# user = User(
#     books=ListField(
#         name='books'
#         value=['a', 'b'],
#         cost=10),
#     music=ListField(...),
#     ...,
# )


class SearchParams:
    """
    Defines user`s properties
    """
    def __init__(
            self, interests, books, movies, music, city,
            interests_cost, books_cost, movies_cost, city_cost,
    ):
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


class BaseField:

    mytype = str

    def __init__(self, name, value, weight):
        self.check_type_name(name)
        self.check_type_value(value)
        self.check_type_weight(weight)

        self.name = name
        self.value = value
        self.weight = weight

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
