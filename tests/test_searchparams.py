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



        #
    # def test_check_type_name_wrong(self):
    #     self.assertFalse(type(self.name) is not str)
    #
    # def test_check_type_value_ok(self):
    #     self.assertTrue(type(self.value) is list or dict)
    #
    # def test_check_type_value_wrong(self):
    #     self.assertFalse(type(self.value) is not list or not dict)
    #
    # def test_check_type_weight_ok(self):
    #     self.assertTrue(type(self.weight) is int)
    #
    # def test_check_type_weight_wrong(self):
    #     self.assertFalse(type(self.weight) is not int)

    # def test_check_type_name_wrong(self):
    #     assert evaluators.Child.check_type_name(2)
    #

