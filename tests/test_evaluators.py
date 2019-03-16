import unittest

from vkinder import evaluators


class TestEvaluators(unittest.TestCase):

    def test_list_xsections_ok(self):
        assert evaluators.list_xsections(['a', 'b'], ['a', 'c']) == ['a']

    def test_list_xsections_empty(self):
        assert evaluators.list_xsections([], ['a', 'c']) == []

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

    # tests for music

    def test_eval_music_match(self):
        assert evaluators.eval_music(['Guitar, Skate, pop-punk'],
                                    ['Guitar, Skate, pop-punk'],
                                     1) == 10

    def test_eval_music_mymusic_not_set(self):
        assert evaluators.eval_music(['Guitar, Skate, pop-punk'],
                                    [''], 1) == 0

    def test_eval_music_music_not_set(self):
        assert evaluators.eval_music([''],
                                    ['Guitar, Skate, pop-punk'], 1) == 0

    def test_eval_music_different_music(self):
        assert evaluators.eval_music(['Guitar'],
                                    ['Punk'], 1) == 0

# tests for interests

    def test_eval_interests_match(self):
        assert evaluators.eval_interests(['Concerts, Aliens, XBox 360'],
                                    ['Concerts, Aliens, XBox 360'], 1) == 10

    def test_eval_interests_myinterests_not_set(self):
        assert evaluators.eval_interests(['Guitar, Skate, pop-punk'],
                                    [''], 1) == 0

    def test_eval_interests_interests_not_set(self):
        assert evaluators.eval_interests([''],
                                    ['Guitar, Skate, pop-punk'], 1) == 0

    def test_eval_interests_different_interests(self):
        assert evaluators.eval_interests(['Guitar'],
                                    ['Punk'], 1) == 0

