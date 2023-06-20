from datetime import time

import pytest


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    if time(hour=6) < current_time < time(hour=22):
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


@pytest.mark.parametrize('current_time, dark_theme_enabled_by_user, res_is_dark_theme', [(time(hour=16), True, True),
                                                                                         (time(hour=23), True, True),
                                                                                         (time(hour=23), None, True),
                                                                                         (time(hour=16), False, False),
                                                                                         (time(hour=23), False, False),
                                                                                         (time(hour=16), None, False)])
def test_dark_theme_by_time_and_user_choice(current_time, dark_theme_enabled_by_user, res_is_dark_theme):
    """
    с 22 до 6 часов утра - ночь
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    is_dark_theme = None
    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
    elif dark_theme_enabled_by_user is None:
        if not time(hour=6) < current_time < time(hour=22):
            is_dark_theme = True
        else:
            is_dark_theme = False
    assert is_dark_theme is res_is_dark_theme


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    for v in users:
        if v['name'] == 'Olga':
            suitable_users = v

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for v in users:
        if v['age'] < 20:
            suitable_users.append(v)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def print_name_def(def_name, *args):
    result = f"{def_name.title().replace('_', ' ')} [{', '.join(args)}]"
    print(result)
    return result


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_name_def(open_browser.__name__, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_name_def(go_to_companyname_homepage.__name__, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_name_def(find_registration_button_on_login_page.__name__, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
