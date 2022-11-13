import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Задача №1 ------------------------------------------------------------------------------------------------------------
def filter_geo_logs(dirty_geo_logs, target_country):
    for visit in list(dirty_geo_logs):
        for city, country in visit.values():
            if country != target_country:
                dirty_geo_logs.remove(visit)

    return dirty_geo_logs

def unic_geo(dirty_ids):
    unic_id = set()
    for user, id in dirty_ids.items():
        unic_id = unic_id.union(id)

    return list(unic_id)

def sort_stats(unsorted_stats):
    sorted_keys_stats = sorted(unsorted_stats, key=unsorted_stats.get)

    return sorted_keys_stats[-1]

# Задача №2 ------------------------------------------------------------------------------------------------------------
def create_folder(token, folder_name):
    create_folder_api_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': folder_name}
    response = requests.put(create_folder_api_url, params=params, headers=headers)
    if response.status_code == 201:
        print('Папка успешно создана')
    else:
        print(f"Ошибка! {response.json()['message']}")
    return response.status_code

def delete_folder(token, folder_name):
    delete_folder_api_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': folder_name}
    response = requests.delete(delete_folder_api_url, params=params, headers=headers)
    if response.status_code == 204:
        print('Папка успешно удалена')
    else:
        print(f"Ошибка! {response.json()['message']}")
    return response.status_code

# Задача №3 ------------------------------------------------------------------------------------------------------------
def ya_login_success(login, password):
    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/')
    login_field = driver.find_element(By.NAME, 'login')
    login_field.send_keys(login)
    driver.find_element(By.ID, 'passp:sign-in').click()
    driver.implicitly_wait(3)
    if driver.find_elements(By.ID, 'field:input-login:hint'):
        print('Такой логин не подойдет')
        return False
    pass_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'passp-field-passwd')))
    pass_field.send_keys(password)
    driver.find_element(By.ID, 'passp:sign-in').click()
    driver.implicitly_wait(3)
    if driver.find_elements(By.ID, 'field:input-passwd:hint'):
        print('Неверный пароль')
        return False
    elif driver.current_url == 'https://id.yandex.ru/':
        print('Успешная авторизация')
        return True
