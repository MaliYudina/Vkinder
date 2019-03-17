"""
Module оценивает (текстовые/строчные) свойства пользователя:
- интересы
- города
- музыку
- книги
- фильмы

Анализ близости значений строчных объектов


"""


def eval_lists(one: list, another: list, cost=1) -> int:
    common = []
    for elem in one:
        if elem in another:
            common.append(elem)
    weight = cost * len(common)
    return weight


def eval_city(city, mycity, cost=10):
    """
    evaluate city location in relation to `mycity`
    :return: integer (cost)
    """
    match_factor = 10
    # City was not set either in original user`s props
    # or the user that we are evaluating
    if not mycity or not city:
        return 0
    if city == mycity:
        return match_factor * cost
    return 0

