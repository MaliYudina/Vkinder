"""
evaluators module evaluates the weight of common string parameters, such as:
interests, city, music, books, movies
Returns final weight of a parameter
"""


def eval_lists(one: list, another: list, cost=1) -> int:
    """
    :param one: a list of interests of a target user
    :param another: a list of interests of a source user
    :param cost: total weight of one parameter for a pair
     (source user + target user)
    :return: integer weight
    """
    common = []
    for elem in one:
        if elem in another:
            common.append(elem)
    weight = cost * len(common)
    return weight


def eval_city(city, mycity, cost=10):
    """
    evaluate city value of a target user with source user's city
    :return: integer (weight)
    """
    match_factor = 10
    # City was not set either in original user`s props
    # or the user that we are evaluating
    if not mycity or not city:
        return 0
    if city == mycity:
        return match_factor * cost
    return 0
