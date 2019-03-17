"""
Module оценивает (текстовые\строчные) свойства пользователя:
- интересы
- города
- музыку
- книги
- фильмы

Анализ близости значений строчных объектов


"""
get_name = 'music'
get_value_dict = {'id': 1, 'title': 'Москва'}
get_value_list = ['Pop-Punk', 'punk', 'punk rock', 'hardcore']
get_weight = 1


props_dict = {
    'name': get_name,
    'value': get_value_list,
    'weight': get_weight,
}


def eval_lists(one: list, another: list) -> int:
    match_factor = 10
    common = []
    for elem in one:
        if elem in another:
            common.append(elem)
    weight = match_factor * len(common)
    return weight




def list_xsections(one: list, another: list) -> list:
    """
    Function compares two lists, returns a new list which represents common elements
    """
    common = []
    for elem in one:
        if elem in another:
            common.append(elem)
    return common


def eval_city(city, mycity, basecost):
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
        return match_factor * basecost
    return 0


# def eval_interests(interests, myinterest, basecost):
#     """
#     evaluate interest of the target user and potential candidates
#     :return: integer (cost)
#     """
#     match_factor = 10
#     if not interests or not myinterest:
#         return 0
#     if interests == myinterest:
#         return match_factor * basecost
#     return 0
#
#
# def eval_music(music, mymusic, basecost):
#     """
#     evaluate music of the target user and potential candidates
#     :return: integer (cost)
#     """
#     match_factor = 10
#     if not music or not mymusic:
#         return 0
#     if music == mymusic:
#         return match_factor * basecost
#     return 0
#
#
# def eval_books(books, mybooks, basecost):
#     """
#     evaluate books of the target user and potential candidates
#     :return: integer (cost)
#     """
#     if not books or not mybooks:
#         raise Exception('a: %s, b: %s' % (books, mybooks))
#         return 0
#     common = list_xsections(books, mybooks)
#     if not common:
#         return 0
#     return len(common) * basecost
#
#
# def eval_movies(movies, mymovies, basecost):
#     """
#     evaluate movies of the target user and potential candidates
#     :return: integer (cost)
#     """
#     match_factor = 10
#     if not movies or not mymovies:
#         return 0
#     if movies == mymovies:
#         return match_factor * basecost
#     return 0
