import unittest
import pytest

from vkinder.vk.user import User


class TestUser(unittest.TestCase):

    def test_create_user(self):
        user = User(
            interests=['a', 'b'],
            movies=['a', 'b'],
            books=['a', 'b'],
            music=['a', 'b'],
            city='a',
        )
        assert user.interests == ['a', 'b']

    def test_user_wrong_params(self):
        with pytest.raises(TypeError):
            User(
                interests='a',
                movies=['a', 'b'],
                books=['a', 'b'],
                music=['a', 'b'],
                city=['a']
            )