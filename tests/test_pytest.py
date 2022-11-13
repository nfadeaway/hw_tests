import pytest

from main import create_folder, delete_folder, ya_login_success

FIXTURE_CREATE_FOLDER = [
    ('real_token', 'new_folder', 201),
    ('wrong_token', 'new_folder', 401),
    ('real_token', 'new_folder', 409)
]

FIXTURE_YA_LOGIN_SUCCESS = [
    ('real_login', 'real_pass', True),
    ('wrong_login', 'wrong_pass', False),
    ('real_login', 'wrong_pass', False)
]

# В ФИКСТУРУ НУЖНО ВНЕСТИ РЕАЛЬНЫЙ ТОКЕН ВМЕСТО real_token
@pytest.mark.parametrize('ya_token, folder_name, etalon', FIXTURE_CREATE_FOLDER)
def test_create_folder(ya_token, folder_name, etalon):
    result = create_folder(ya_token, folder_name)
    assert result == etalon
    if result == 409:
        delete_folder(ya_token, folder_name)

# В ФИКСТУРУ НУЖНО ВНОСИТЬ РЕАЛЬНЫЕ ДАННЫЕ ВМЕСТО real_login И real_pass
@pytest.mark.parametrize('login, password, etalon', FIXTURE_YA_LOGIN_SUCCESS)
def test_ya_login_success(login, password, etalon):
    result = ya_login_success(login, password)
    assert result == etalon
