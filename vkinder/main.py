"""
По заданному диапазону получаем результаты в виде пользователей (ID + баллы соответсвия) из
результатов поиска по диапазону:
- свои друзья
- подписчики
- пользователи общих групп
"""
from typing import List
import operator

from vkinder.searchparams import SearchParams
from .field_adapters import dummy, city_to_string, split_string
from .evaluators import eval_lists, eval_city

EVALUATORS = {
    'city': eval_city,
    'interests': eval_lists,
    'music': eval_lists,
    'books': eval_lists,
    'movies': eval_lists,
}
ADAPTERS = {
    'city': city_to_string,
    'interests': split_string,
    'music': split_string,
    'books': split_string,
    'movies': split_string,

}


def top_n(search_params: SearchParams, candidates: List[dict], number=3) -> List[int]:
    """
    1. Get users candidates
    2. For each user_raw in candidates, fire up all evaluators.
     Result is written into a separate dictionary, which will be returned.
    """
    matches = dict()

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
    # [(17300535, 200), (2128351, 100), (2677959, 0)]
    sorted_matches = sorted(matches.items(), key=operator.itemgetter(1), reverse=True)
    return [x for x, y in sorted_matches[0:number]]
