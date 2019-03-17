import unittest
import pytest

from vkinder import searchparams as sp
from vkinder.main import top_n


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

users = [
    {
    "id": 9714,
    "first_name": "Марина",
    "last_name": "Маури",
    "domain": "id9714",
    "bdate": "10.1",
    "city": {
        "id": 198,
        "title": "Wien"
    },
    "photo_big": "https://pp.userapi.com/bMHYazE4YPstobZ5HpQeJtFwW1cxEB4hcngumQ/UkX0yRi0oYs.jpg?ava=1",
    "interests": "фитнес, тайбо, немецкий язык, мода и стиль, кофе, межкультурная коммуникация, психология общения, Suomi, языки, Германия, работа, поезда, плюшевые мишки, Москва, беседы по душам, успех, коты, CША, отпуск в одиночестве, сумерки, EU, путешествия, темный шоколад, вечера при свечах, театр, ирония, финский язык, ощущения, зеленый чай, ожидание хорошего, стильные люди, Скандинавия, романтика, тренинги, искренность, svenska, орхидеи, большие города",
    "online": 0
    },
    {
    "id": 30518,
    "first_name": "Антон",
    "last_name": "Попович",
    "domain": "batony4",
    "bdate": "20.6.1984",
    "city": {
        "id": 2,
        "title": "Санкт-Петербург"
    },
    "photo_big": "https://pp.userapi.com/c638821/v638821518/13fb8/jqAyR2oQdz8.jpg?ava=1",
    "interests": "Рок, Ролики, Коньки, Ночь, Крыши, Гитара, Музыка, Питер, Фотография, PhotoShop, Общественная деятельность, Походы, Природа, Недострои и дестрои, Dead-Line, Код Опасности, NightFest, Экстрим, Скорость, Сноуборд, Картинг, Пеинтбол, Q-Zar, Волейбол, Футбол, Настольный теннис, Бильярд, Го, Мафия, Покер, Текила, Малибу, Кальян, Глинтвейн, Пиво, Программирование, ACM, TopCoder, Web-Дизайн",
    "online": 0
}
]

class TestTop(unittest.TestCase):
    def test_top_n(self):
        search = sp.SearchParams([
            sp.ListField(name='interests', value=['тайбо'], weight=500),
            sp.StringField(name='city', value='Санкт-Петербург', weight=10),
        ])
        assert top_n(search, users, number=1) == []  # TODO вернуть значения

    def test_top_n_wrong(self):
        search = sp.SearchParams([
            sp.ListField(name='books', value=['Ремарк'], weight=100),
            sp.StringField(name='city', value='Москва', weight=10),
        ])
        with pytest.raises(Exception):
            assert top_n(search, SAMPLE_VK_RESP) == [
                (2128351, 100), (2677959, 0), (17300535, 200)
            ]



