import pytest

from main import create_folder, delete_folder, ya_login_success

FIXTURE_CREATE_FOLDER = [
    ('верный_токен', 'new_folder', 201),
    ('неверный_токен', 'new_folder', 401),
    ('верный_токен', 'new_folder', 409)
]

FIXTURE_YA_LOGIN_SUCCESS = [
    ('реальный логин', 'реальный пароль', True),
    ('несуществующий логин', 'неверный пароль', False),
    ('реальный логин', 'неверный пароль', False)
]

# В ФИКСТУРУ НУЖНО ВНЕСТИ РЕАЛЬНЫЙ ТОКЕН ВМЕСТО верный_токен
@pytest.mark.parametrize('ya_token, folder_name, etalon', FIXTURE_CREATE_FOLDER)
def test_create_folder(ya_token, folder_name, etalon):
    result = create_folder(ya_token, folder_name)
    assert result == etalon
    if result == 409:
        delete_folder(ya_token, folder_name)

# В ФИКСТУРУ НУЖНО ВНОСИТЬ РЕАЛЬНЫЕ ДАННЫЕ ГДЕ НЕОБХОДИМО
@pytest.mark.parametrize('login, password, etalon', FIXTURE_YA_LOGIN_SUCCESS)
def test_ya_login_success(login, password, etalon):
    result = ya_login_success(login, password)
    assert result == etalon
