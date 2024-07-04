import requests
from ..api_tests.generator import random_name
import allure


@allure.feature('Profile page')
@allure.story('Retrieve users data')
def test_user_me(base_api_url, access_token, credentials):
    path = "/api/v1/auth/users/me/"

    with allure.step('Retrieve users data from API'):
        user_me_response = requests.get(url=base_api_url + path, 
                                    headers={'Authorization': access_token.get('Authorization')})
        json_user_me_data = user_me_response.json()

    with allure.step('Check the 200 status response'):
        assert user_me_response.status_code == 200
    with allure.step('Check the blank object response'):
        assert json_user_me_data != {}
    with allure.step('Verify username in the response'):
        assert credentials.get('username') == json_user_me_data.get('username')


@allure.feature('Profile page')
@allure.story('Change users data')
def test_change_user_data(base_api_url, access_token):
    path = "/api/v1/profile/"
    
    with allure.step('Generate random users data'):
        json_random_data = random_name()

    with allure.step('Change users data using generated data'):
        changed_user_data_response = requests.patch(url=base_api_url + path, 
                                    headers={'Authorization': access_token.get('Authorization')}, 
                                    json={'first_name': json_random_data.get('first_name'), 'last_name': json_random_data.get('last_name'), 
                                    'patronymic': json_random_data.get('patronymic'), 'phone': json_random_data.get('phone')})
        response_changed_data = changed_user_data_response.json()

    with allure.step('Check the 200 status response'):
        assert changed_user_data_response.status_code == 200
    with allure.step('Check the blank object response'):
        assert changed_user_data_response != {}
    with allure.step('Verify users data in the response'):
        with allure.step('Verify first_name in the response'):
            assert json_random_data.get('first_name') == response_changed_data.get('first_name')
        with allure.step('Verify last_name in the response'):
            assert json_random_data.get('last_name') == response_changed_data.get('last_name')
        with allure.step('Verify patronymic in the response'):
            assert json_random_data.get('patronymic') == response_changed_data.get('patronymic')
        with allure.step('Verify phone in the response'):
            assert json_random_data.get('phone') == response_changed_data.get('phone')


@allure.feature('Profile page')
@allure.story('Change users password')
def test_change_users_password(base_api_url, access_token, credentials):
    path = "/api/v1/auth/users/set_password/"

    password = '1qwe2qaz'
    
    with allure.step('Change users password'):
        changed_user_password_response = requests.post(url=base_api_url + path, 
                                    headers={'Authorization': access_token.get('Authorization')}, 
                                    json={'current_password': credentials.get('password'), 'new_password': password, 
                                    're_new_password': password})
    
    with allure.step('Check the 204 status response'):
        assert changed_user_password_response.status_code == 204

    with allure.step('Check whether changed password works'):
        token_response = requests.post(url=base_api_url + "/api/v1/auth/jwt/create/", json={"username": "test@ya.ru", "password": password},
                            verify=False)
    with allure.step('Check the 200 status response of auth'):
        assert token_response.status_code == 200
    
