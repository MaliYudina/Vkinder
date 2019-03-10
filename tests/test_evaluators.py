import unittest

from vkinder import evaluators


class TestEvaluators(unittest.TestCase):

    def test_eval_city_match(self):
        assert evaluators.eval_city('spb', 'spb') == 10

    def test_eval_city_mycity_not_set(self):
        assert evaluators.eval_city('spb', '') == 0

    def test_eval_city_different_city(self):
        assert evaluators.eval_city('spb', 'москва') == 0

    def test_eval_city_mycity_dict_not_set(self):
        assert evaluators.eval_city(
            {'id': 1, 'title': 'Москва'}, None) == 0

    def test_eval_city_mycity_dict(self):
        assert evaluators.eval_city(
            {'id': 1, 'title': 'Москва'},
            {'id': 2, 'title': 'спб'}
        ) == 0
