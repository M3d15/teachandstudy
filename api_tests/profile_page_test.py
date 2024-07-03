import requests
from ..api_tests.generator import random_name

def test_user_me(base_api_url, access_token, credentials):
    path = "/api/v1/auth/users/me/"

    user_me_response = requests.get(url=base_api_url + path, 
                                 headers={'Authorization': access_token.get('Authorization')})
    
    json_user_me_data = user_me_response.json()

    assert user_me_response.status_code == 200
    assert json_user_me_data != {}
    assert credentials.get('username') == json_user_me_data.get('username')


def test_change_user_data(base_api_url, access_token):
    path = "/api/v1/profile/"

    json_random_data = random_name()
    
    changed_user_data_response = requests.patch(url=base_api_url + path, 
                                 headers={'Authorization': access_token.get('Authorization')}, 
                                 json={'first_name': json_random_data.get('first_name'), 'last_name': json_random_data.get('last_name'), 
                                 'patronymic': json_random_data.get('patronymic'), 'phone': json_random_data.get('phone')})
    response_changed_data = changed_user_data_response.json()

    assert changed_user_data_response.status_code == 200
    assert changed_user_data_response != {}
    assert json_random_data.get('first_name') == response_changed_data.get('first_name')
    assert json_random_data.get('last_name') == response_changed_data.get('last_name')
    assert json_random_data.get('patronymic') == response_changed_data.get('patronymic')
    assert json_random_data.get('phone') == response_changed_data.get('phone')


def test_change_users_password(base_api_url, access_token, credentials):
    path = "/api/v1/auth/users/set_password/"

    password = '1qwe2qaz'
    
    changed_user_password_response = requests.post(url=base_api_url + path, 
                                 headers={'Authorization': access_token.get('Authorization')}, 
                                 json={'current_password': credentials.get('password'), 'new_password': password, 
                                 're_new_password': password})
    
    assert changed_user_password_response.status_code == 204

    token_response = requests.post(url=base_api_url + "/api/v1/auth/jwt/create/", json={"username": "test@ya.ru", "password": password},
                         verify=False)
    
    assert token_response.status_code == 200
    
