"""
Module оценивает (текстовые\строчные) свойства пользователя:
- интересы
- города
- музыку
- книги
- фильмы

Анализ близости значений строчных объектов


"""


def eval_city(city, mycity):
    """
    evaluate city location in relation to `mycity`
    :return: integer (cost)
    """
    basecost = 1
    match_factor = 10
    # City was not set either in original user`s props
    # or the user that we are evaluating
    if not mycity or not city:
        return 0
    if city == mycity:
        return match_factor * basecost
    return 0
