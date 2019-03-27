"""
run module communicates with user input for the following initialization
of main module
"""
from vkinder.searchparams import SearchParams, StringField, ListField
from vkinder.vk import search, MALE, get_photos
from vkinder.main import data_process, sort_data
import time


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
        StringField(name='city', value='Самара', weight=50),
        ListField(name='books', value=['Ремарк'], weight=100),
        ListField(name='movies', value=['Матрица'], weight=200),
        ListField(name='interests', value=['фитнес'], weight=150),
    ])

    candidates = search(
        login=vk_login,
        password=vk_pw,
        fields=list(params.registry),
        age_min=age_min,
        age_max=age_max,
        sex=MALE,
    )

    top_10_candidates = data_process(search_params=params, candidates=candidates)
    sorted_result = sort_data(top_10_candidates)
    sorted_top_10 = list(sorted_result)[0:10]

    for candidate in sorted_top_10:
        time.sleep(0.5)
        photos = get_photos(
            login=vk_login,
            password=vk_pw,
            owner_id=candidate,
        )
        photos_dict = dict()
        for photo in photos:
            likes = photo['likes']['count']
            for size in photo['sizes']:
                if size['type'] == 'x':
                    url = size['url']
            photos_dict[url] = likes
        top3_photos = sorted(photos_dict.items(), key=lambda x: x[1], reverse=True)[0:3]
        print('Топ 3 фото для id', candidate, top3_photos)

    print('Done!')


if __name__ == '__main__':
    _main()
