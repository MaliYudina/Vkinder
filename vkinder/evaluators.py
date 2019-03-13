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


def eval_city(city, mycity, basecost=1):
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


def eval_interests(interests, myinterest):
    """
    evaluate interest of the target user and potential candidates
    :param interests:
    :param myinterest:
    :return: integer (cost)
    """
    basecost = 1
    match_factor = 10
    if not interests or not myinterest:
        return 0
    if interests == myinterest:
        return match_factor * basecost
    return 0


def eval_music(music, mymusic):
    """
    evaluate music of the target user and potential candidates
    :param music:
    :param mymusic:
    :return: integer (cost)
    """
    basecost = 1
    match_factor = 10
    if not music or not mymusic:
        return 0
    if music == mymusic:
        return match_factor * basecost
    return 0


def eval_books(books, mybooks):
    """
    evaluate books of the target user and potential candidates
    :param books:
    :param mybooks:
    :return: integer (cost)
    """
    basecost = 1
    match_factor = 10
    if not books or not mybooks:
        return 0
    if books == mybooks:
        return match_factor * basecost
    return 0


def eval_movies(movies, mymovies):
    """
    evaluate movies of the target user and potential candidates
    :param movies:
    :param mymovies:
    :return: integer (cost)
    """
    basecost = 1
    match_factor = 10
    if not movies or not mymovies:
        return 0
    if movies == mymovies:
        return match_factor * basecost
    return 0
