"""
Main module initiates the search of the target user by calling other modules
"""
from typing import List
import json
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


def data_process(search_params: SearchParams, candidates: List[dict]) -> dict:
    """
    Get matched candidates, each user_raw processed by evaluators and adapters.
    Result is written as list of IDs.
    """
    assert isinstance(candidates, list)
    data = dict()

    # Look at each user_raw in the candidates individually.
    for user_raw in candidates:
        # Process EVALUATORS keys ('city')
        weight = 0
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

            weight += evaluator(
                adapter(user_raw[field]),
                field_obj.value,
                field_obj.weight,
            )

        data[user_raw['id']] = {'weight': weight, 'user': user_raw}

        filename = 'data_answer.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data,
                               sort_keys=False,
                               indent=4,
                               ensure_ascii=False,
                               separators=(',', ': ')))

    return data


def sort_data(data):
    sort_list = {}
    for uid, user in data.items():
        sort_list[uid] = user['weight']

    filename = 'sorted_weight.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(sort_list,
                           sort_keys=False,
                           indent=4,
                           ensure_ascii=False,
                           separators=(',', ': ')))
    return sort_list




# return [uid for uid, _ in sorted_matches[0:number]]

# получаем список групп пользователя
# если мэтч юзер имеет группу такую же - кладем в обший список
# for user in group


def groups_matching():
    pass
