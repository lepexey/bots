import pprint

import vk_api


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция. """

    # Код двухфакторной аутентификации,
    # который присылается по смс или уведомлением в мобильное приложение
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main():
    login, password = "89173834745", ""
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=3, offset=1)
    if response['items']:
        for i in response['items']:
            print(i)

    friends_print = 0
    response = vk.wall.get(count=5)
    response_friends = vk.friends.get(fields="bdate, city")
    responce_user = vk.users.get(screen_name="lirapchelova")
    print("==========POSTS================================")
    if response['items']:
        for i in response['items']:
            print(i['post_type'], "| type:", i['attachments'][0]['type'])
    print("==========FRIENDS==============================")
    if response_friends['items']:
        for i in response_friends['items']:
            print(i["first_name"], end='  ')
            if friends_print == 10:
                print()
    print()
    print("==========USER=================================")
    pprint.pprint(responce_user[0])


if __name__ == '__main__':
    main()
