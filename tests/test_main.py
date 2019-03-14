import unittest

from vkinder import searchparams as sp
from vkinder.main import top_n


class TestTop(unittest.TestCase):
    def test_top_n(self):
        search = sp.SearchParams([
            sp.ListField(name='books', value=['Ремарк'], weight=100),
            sp.StringField(name='city', value='Москва', weight=10),
        ])
        assert top_n(search) == {}
