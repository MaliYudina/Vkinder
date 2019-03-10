"""
По заданному диапазону получаем результаты в виде пользователей (ID + баллы соответсвия) из
результатов поиска по диапазону:
- свои друзья
- подписчики
- пользователи общих групп
"""
from .vk.user import User
from .vk import api
from .evaluators import eval_city
from typing import Dict
from .field_adapters import dummy, city_to_string


EVALUATORS = {
    'city': eval_city,
}

ADAPTERS = {
    'city': city_to_string,
}


def top_n(target_user: User) -> Dict[str, int]:
    """
    1. Get users pool
    2. For each user in pool, fire up all evaluators.
     Result is written into a separate dictionary, which will be returned.
    """
    matches = dict()

    pool = api.search(
        target_user.interests,
        target_user.movies,
    )
    # Pool will be something like:
    # [{'bdate': '1.11.1901',
    #  'books': 'words, words, words',
    #  'can_access_closed': True,
    #  'city': {'id': 1, 'title': 'Москва'},
    #  'first_name': 'first',
    #  'id': 1,
    #  'interests': 'Guitar, Skate, pop-punk, Concerts, Aliens, XBox 360, PS3, Wii'
    #  'is_closed': False,
    #  'last_name': 'last',
    #  'movies': 'a lot',
    #  'music': 'Pop-Punk, punk, punk rock, hardcore, blues, funk, jazz',
    #  'photo_big': ...
    # ... ]

    # Look at each user in the pool individually.
    for user in pool:
        # Process EVALUATORS keys ('city')
        for field, evaluator in EVALUATORS.items():
            # field = e.g. 'city'
            # evaluator = e.g. 'city_to_string'
            if not user.get(field):
                continue

            # Get a matching adapter from available list.
            # If none found, use default ("dummy"), which transparently returns the value as-is.
            adapter = ADAPTERS.get(
                field, dummy)

            cost = evaluator(
                adapter(user[field]),
                getattr(target_user, field)
            )
            try:
                matches[user['id']] += cost
            except KeyError:
                matches[user['id']] = cost
    return matches
