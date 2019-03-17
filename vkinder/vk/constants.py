"""
Constants модуль с описанием констант (URL адреса) для обращения к Vk API
"""

# GET_USER = 'vkapi.user.get'
# GET_FRIENDS = 'vkapi.friends.get'
# GET_GROUPS = 'vkapi.groups.get'
# USER_SEARCH = 'vkapi.users.search'
# GET_PHOTOS = 'vkapi.photos.get'


class Constants:
    # Идентификатор моего пользователя вконтакте
    MY_USER_ID = 675274
    # Общая ссылка для доступа к api
    API_URL = 'https://api.vk.com/method/'
    # Идентификатор приложения вконтакте
    APP_ID = 6776462
    # Логин пользователя ВКонтакет
    LOGIN = '89310083415'
    VERSION = 5.92
    TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'

    # # Мой пароль вконтакте
    # @staticmethod
    # def GET_PASSWORD():
    #     f = open('pass.txt','r')
    #     PASSWORD = f.read().rstrip()
    #     f.close()
    #     return PASSWORD


if __name__ == '__main__':
    PASSWORD = Constants.GET_PASSWORD()
