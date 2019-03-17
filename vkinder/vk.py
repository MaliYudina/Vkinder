"""
API модуль для вызова Вк, используя методы (get, search, etc) чтобы получить ответ в виде данных
о пользователе (имя, возраст, интересы и тп)
"""
import vk

APP_ID = 6776462
VERSION = 5.92
MALE = 2
FEMALE = 1


def search(login, password, fields, age_min, age_max, sex) -> list:
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password)
    vkapi = vk.API(session)

    return vkapi.users.search(
        v=VERSION,
        count=1000,
        sex=sex,
        age_from=age_min,
        fields=','.join(fields),
        age_to=age_max)
