"""
Vk API returns random format results.
Field_adapters module performs data normalization
"""
from typing import List


DEFAULT_RS = ','


def city_to_string(city: dict) -> str:
    """
    From dict value return string value of the city
    {'id': 1, 'title': 'Москва'} --> 'Москва'
    """
    return city['title']


def split_string(string: str) -> List[str]:
    """
    From simple string return List of strings
    """
    parts = string.split(DEFAULT_RS)
    for i, part in enumerate(parts):
        parts[i] = part.strip()
    return parts


def dummy(anything):
    """
    Returns value anyway
    """
    return anything
