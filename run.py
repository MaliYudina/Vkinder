"""
run module communicates with user input for the following initialization
of main module
"""
from vkinder.searchparams import SearchParams, StringField, ListField
from vkinder.vk import search, MALE
from vkinder.main import data_process, sort_data


def _main():
    """
    get user's input of login, password, filter parameters of a candidate
    """
    # Ask user input?
    vk_login = ''
    vk_pw = ''
    age_min = 18
    age_max = 50

    params = SearchParams([
        StringField(name='city', value='Москва', weight=100),
        ListField(name='books', value=['Ремарк'], weight=10),
        ListField(name='movies', value=['Матрица'], weight=2),
        ListField(name='interests', value=['фитнес'], weight=1),
    ])

    candidates = search(
        login=vk_login,
        password=vk_pw,
        fields=list(params.registry),
        age_min=age_min,
        age_max=age_max,
        sex=MALE,
    )

    top_3 = data_process(search_params=params, candidates=candidates)
    sort_data(top_3)
    print('Top_3:', top_3)



if __name__ == '__main__':
    _main()
