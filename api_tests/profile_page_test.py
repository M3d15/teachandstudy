import requests
from ..api_tests.generator import random_name

def test_user_me(base_api_url, access_token, credentials):
    path = "/api/v1/auth/users/me/"

    user_me_response = requests.get(url=base_api_url + path, 
                                 headers={'Authorization': access_token['Authorization']})
    
    json_user_me_data = user_me_response.json()

    assert user_me_response.status_code == 200
    assert json_user_me_data != {}
    assert credentials['username'] == json_user_me_data['username']


def test_change_user_data(base_api_url, access_token):
    path = "/api/v1/profile/"

    json_random_data = random_name()
    
    changed_user_data_response = requests.patch(url=base_api_url + path, 
                                 headers={'Authorization': access_token['Authorization']}, 
                                 json={'first_name': json_random_data['first_name'], 'last_name': json_random_data['last_name'], 
                                 'patronymic': json_random_data['patronymic'], 'phone': json_random_data['phone']})
    response_changed_data = changed_user_data_response.json()

    assert changed_user_data_response.status_code == 200
    assert changed_user_data_response != {}
    assert json_random_data['first_name'] == response_changed_data['first_name']
    assert json_random_data['last_name'] == response_changed_data['last_name']
    assert json_random_data['patronymic'] == response_changed_data['patronymic']
    assert json_random_data['phone'] == response_changed_data['phone']
