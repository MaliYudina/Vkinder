import unittest

from vkinder import evaluators


class TestEvaluators(unittest.TestCase):

    def test_eval_city_match(self):
        assert evaluators.eval_city('spb', 'spb', 1) == 10

    def test_eval_city_mycity_not_set(self):
        assert evaluators.eval_city('spb', '', 1) == 0

    def test_eval_city_different_city(self):
        assert evaluators.eval_city('spb', 'москва', 1) == 0

    def test_eval_city_mycity_dict_not_set(self):
        assert evaluators.eval_city(
            {'id': 1, 'title': 'Москва'}, None, 1) == 0

    def test_eval_city_mycity_dict(self):
        assert evaluators.eval_city(
            {'id': 1, 'title': 'Москва'},
            {'id': 2, 'title': 'спб'},
            1
        ) == 0

# tests for other lists (interests, movies, books or whatever)

    def test_eval_lists_match(self):
        assert evaluators.eval_lists(['Concerts, Aliens, XBox 360'],
                                    ['Concerts, Aliens, XBox 360'], 1) == 1

    def test_eval_lists_mylist_not_set(self):
        assert evaluators.eval_lists(['Guitar, Skate, pop-punk'],
                                    [''], 1) == 0

    def test_eval_lists_not_set(self):
        assert evaluators.eval_lists([''],
                                    ['Guitar, Skate, pop-punk'], 1) == 0

    def test_eval_lists_different(self):
        assert evaluators.eval_lists(['Guitar'],
                                    ['Punk'], 1) == 0
