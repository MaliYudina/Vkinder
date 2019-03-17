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
    parts = string.split(DEFAULT_RS)
    for i, part in enumerate(parts):
        parts[i] = part.strip()
    return parts


def dummy(anything):
    return anything
