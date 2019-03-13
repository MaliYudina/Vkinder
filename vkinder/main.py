"""
По заданному диапазону получаем результаты в виде пользователей (ID + баллы соответсвия) из
результатов поиска по диапазону:
- свои друзья
- подписчики
- пользователи общих групп
"""
from vkinder.searchparams import SearchParams
from .vk import api
from .evaluators import eval_city, eval_interests, eval_music, eval_books, eval_movies
from typing import Dict
from .field_adapters import dummy, city_to_string, split_string


EVALUATORS = {
    'city': eval_city,
    'interests': eval_interests,
    'music': eval_music,
    'books': eval_books,
    'movies': eval_movies,

}

ADAPTERS = {
    'city': city_to_string,
    'interests': split_string,
    'music': split_string,
    'books': split_string,
    'movies': split_string,

}


def top_n(target_user: SearchParams) -> Dict[str, int]:
    """
    1. Get users pool
    2. For each user in pool, fire up all evaluators.
     Result is written into a separate dictionary, which will be returned.
    """
    matches = dict()

    pool = api.search(
        target_user.city,
        target_user.interests,
        target_user.movies,
        target_user.books,
        target_user.movies
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

            field_obj = getattr(target_user, field)

            # Get a matching adapter from available list.
            # If none found, use default ("dummy"), which transparently returns the value as-is.
            adapter = ADAPTERS.get(
                field, dummy)

            cost = evaluator(
                adapter(user[field]),
                field_obj.value  # NOTE: if changed into class, need to access an attribute, not class itself
            )
            try:
                matches[user['id']] += cost
            except KeyError:
                matches[user['id']] = cost
    return matches
