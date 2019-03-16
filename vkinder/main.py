"""
По заданному диапазону получаем результаты в виде пользователей (ID + баллы соответсвия) из
результатов поиска по диапазону:
- свои друзья
- подписчики
- пользователи общих групп
"""
import operator
from vkinder.searchparams import SearchParams
from .vk import api
from vkinder.evaluators import eval_city, eval_interests, eval_music, eval_books, eval_movies
from typing import List
from .field_adapters import dummy, city_to_string, split_string



from vkinder.searchparams import EVALUATORS, ADAPTERS


def top_n(search_params: SearchParams, candidates: List[dict], number=3) -> List[int]:
    """
    1. Get users candidates
    2. For each user_raw in candidates, fire up all evaluators.
     Result is written into a separate dictionary, which will be returned.
    """
    matches = dict()


    # дергаем ручку вкапи

    # candidates = api.search(
    #
    # )
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

    # Look at each user_raw in the candidates individually.
    for user_raw in candidates:

        # Process EVALUATORS keys ('city')
        for field, evaluator in EVALUATORS.items():
            # field = e.g. 'city'
            # evaluator = e.g. 'city_to_string'
            if not user_raw.get(field):
                continue

            if not search_params.registry.get(field):
                continue
            field_obj = search_params.registry[field]

            # Get a matching adapter from available list.
            # If none found, use default ("dummy"), which transparently returns the value as-is.
            adapter = ADAPTERS.get(
                field, dummy)

            weight = evaluator(
                adapter(user_raw[field]),
                field_obj.value,
                field_obj.weight,
            )
            try:
                matches[user_raw['id']] += weight
            except KeyError:
                matches[user_raw['id']] = weight
    # return matches
    # список кортежей, отсортированных по второму элементу в каждом кортеже.
    #[(17300535, 200), (2128351, 100), (2677959, 0)]
    sorted_matches = sorted(matches.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_matches[0:number]


