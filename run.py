"""
run module communicates with user input for the following initialization
of main module
"""
from vkinder.searchparams import SearchParams, StringField, ListField
from vkinder.vk import search, MALE, get_photos
from vkinder.main import data_process, sort_data


def _main():
    """
    get user's input of login, password, filter parameters of a candidate
    """
    # Ask user input?
    vk_login = ''
    vk_pw = ''
    age_min = 30
    age_max = 50

    params = SearchParams([
        StringField(name='city', value='Москва', weight=100),
        ListField(name='books', value=['Ремарк'], weight=10),
        ListField(name='movies', value=['Матрица'], weight=50),
        ListField(name='interests', value=['фитнес'], weight=60),
    ])

    candidates = search(
        login=vk_login,
        password=vk_pw,
        fields=list(params.registry),
        age_min=age_min,
        age_max=age_max,
        sex=MALE,
    )

    photos = get_photos(
        login=vk_login,
        password=vk_pw,
        owner_id=1,
    )

    top_n = data_process(search_params=params, candidates=candidates)
    sorted_result = sort_data(top_n)
    ph = photos
    print(ph)
    print('Top candidates sorted by weight: ', list(sorted_result)[0:10])
    print('Done!')


if __name__ == '__main__':
    _main()
