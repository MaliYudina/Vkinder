"""
run module communicates with user input for the following initialization
of main module
"""
from vkinder.searchparams import SearchParams, StringField, ListField
from vkinder.vk import search, MALE
from vkinder.main import top_n


def _main():
    """
    get user's input of login, password, filter parameters of a candidate
    """
    # Ask user input?
    vk_login = 'aa'
    vk_pw = 'aa'
    age_min = 18
    age_max = 50

    params = SearchParams([
        StringField(name='city', value='Санкт-Петербург', weight=100),
        ListField(name='books', value=['Ремарк'], weight=10),
        ListField(name='movies', value=['Матрица', 'Пила'], weight=2),
        ListField(name='interests', value=['Python', 'фитнес'], weight=1),
    ])

    candidates = search(
        login=vk_login,
        password=vk_pw,
        fields=list(params.registry),
        age_min=age_min,
        age_max=age_max,
        sex=MALE,
    )

    top_3 = top_n(search_params=params, candidates=candidates, number=3)
    print(top_3)


if __name__ == '__main__':
    _main()
