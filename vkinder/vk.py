"""
vk module calls to vk, using methods, and parameters (age, city, interests, i.e)
"""
import vk


APP_ID = 6120276
VERSION = 5.92
MALE = 2
FEMALE = 1


def search(login, password, fields, age_min, age_max, sex) -> list:
    """
    :param login: input login of User
    :param password: User's password
    :param fields: fields to use as a filter of common properties
    :param age_min: minimum age of the candidate
    :param age_max: maximum age of the candidate
    :param sex: sex of the required candidate (male/female)
    :return: list of candidates
    """
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password
                             )

    vkapi = vk.API(session)

    return vkapi.users.search(
        v=VERSION,
        count=1000,
        sex=sex,
        age_from=age_min,
        fields=','.join(fields),
        age_to=age_max,
    )['items']


def get_photos(login, password, owner_id) -> list:
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password
                             )

    vkapi = vk.API(session)

    photos_response = vkapi.photos.get(
        v=VERSION,
        count=1000,
        album_id='profile',
        extended=1,
        owner_id=owner_id,
    )['items']

    return photos_response
