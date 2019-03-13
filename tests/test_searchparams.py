import unittest
import pytest

from vkinder import searchparams as sparam


class TestFields(unittest.TestCase):

    def test_check_type_name_not_ok(self):
        with pytest.raises(TypeError):
            sparam.ListField(
                name=1,
                weight=1,
                value=[],
            )

    def test_check_type_name_ok(self):
        sparam.ListField(
            name='a',
            weight=1,
            value=[],
        )

    def test_check_type_weight_not_ok(self):
        with pytest.raises(TypeError):
            sparam.ListField(
                name='a',
                weight='b',
                value=[],
            )

    def test_check_type_weight_ok(self):
        sparam.ListField(
            name='a',
            weight=1,
            value=[],
        )

    def test_check_type_value_not_ok(self):
        with pytest.raises(TypeError):
            sparam.ListField(
                name='a',
                weight=1,
                value={},
            )

    def test_check_type_value_ok(self):
        sparam.ListField(
            name='a',
            weight=1,
            value=[],
        )

    def test_check_type_value_str_not_ok(self):
        with pytest.raises(TypeError):
            sparam.StringField(
                name='a',
                weight=1,
                value={},
            )

    def test_check_type_value_str_ok(self):
        sparam.StringField(
            name='a',
            weight=1,
            value='bb',
        )
