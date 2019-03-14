import unittest
import pytest

from vkinder import field_adapters as fadapter


class TestFieldsAdapters(unittest.TestCase):

    def test_city_to_string_ok(self):
        assert type(fadapter.city_to_string({'id': 1, 'title': 'Москва'})) == str

    def test_city_to_string_wrong_key(self):
        with pytest.raises(KeyError):
            assert fadapter.city_to_string({'id': 1, 'name': 'Москва'})

    def test_split_string_ok(self):
        assert fadapter.split_string('a  b  c d e') == ['a  b  c d e']

    def test_split_string_wrong(self):
        with pytest.raises(AttributeError):
            fadapter.split_string(['a  b  c d e'])

