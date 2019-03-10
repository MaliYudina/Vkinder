"""
Vk API returns random format results.
Field_adapters module performs data normalization
"""

from typing import List


DEFAULT_RS = ','


def city_to_string(city: dict) -> str:
    """
    {'id': 1, 'title': 'Москва'} --> 'Москва'
    """
    return city['title']


def split_string(string: str) -> List[str]:
    # TODO: remove spaces -- str.strip()
    return string.split(DEFAULT_RS)


def dummy(anything):
    return anything
