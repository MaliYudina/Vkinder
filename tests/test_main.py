import unittest

from vkinder import searchparams as sp
from vkinder.main import data_process


SAMPLE_VK_RESP = [{'bdate': '1.11.1989',
      'books': 'сжигаю книги',
      'can_access_closed': True,
      'city': {'id': 1, 'title': 'reutov'},
      'first_name': 'Максим',
      'id': 2677959,
      'interests': 'Guitar, Skate, pop-punk, Concerts, Aliens, XBox 360, PS3, Wii, '
                   'DS, ебашить поп-панк, not to drink, not to smoke, lots of '
                   'stuff',
      'is_closed': False,
      'last_name': 'Голополосов',
      'movies': 'a lot',
      'music': 'Pop-Punk, punk, punk rock, hardcore, blues, funk, jazz',
      'photo_big': 'https://sun9-33.userapi.com/c851132/v851132716/9133d/4d-lIMegM8k.jpg?ava=1'},
     {'bdate': '26.11.1986',
      'books': 'Люциус Шепапрд, Ремарк',
      'can_access_closed': True,
      'city': {'id': 1, 'title': 'Москва'},
      'first_name': 'Александр',
      'id': 17300535,
      'interests': 'Эмоции, Вселенная',
      'is_closed': False,
      'last_name': 'Шепс',
      'movies': '"Окно в париж", "Властелин Колец", "Аватар", " Дитя '
                'Человеческое", "Дежа вю"',
      'music': 'Milen Farmer, Celin Dion, Enigmatica',
      'photo_big': 'https://sun9-6.userapi.com/c850724/v850724998/8f178/Mo4QBUkaAWk.jpg?ava=1'},
     {'bdate': '20.4.1980',
      'books': '"Алхимик Пауло Коэльо", "Хроники Амберы Желязного"',
      'can_access_closed': True,
      'city': {'id': 1, 'title': 'Москва'},
      'first_name': 'Вася',
      'id': 2128351,
      'interests': 'Kитайский Чай, Сноуборд, PavelDura',
      'is_closed': False,
      'last_name': 'Вакуленко',
      'movies': '"Остров", "Облако Рай"',
      'music': 'Wu-tang clan, Ol’dirty Bastard, Busta Rhymes, das MAD lib MF doom '
               'blazy blazy',
      'photo_big': 'https://sun9-34.userapi.com/c848636/v848636782/c48f2/-kP6Z2Px6XM.jpg?ava=1'}]


class TestTop(unittest.TestCase):
    def test_data_process(self):
        search = sp.SearchParams([
            sp.ListField(name='books', value=['Ремарк'], weight=100),
            sp.StringField(name='city', value='Москва', weight=10),
        ])
        assert data_process(search, SAMPLE_VK_RESP) == [
            17300535, 2128351, 2677959,
        ]
