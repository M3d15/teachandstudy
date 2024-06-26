import requests

def test_user_me(base_api_url, access_token, credentials):
    path = "/api/v1/auth/users/me/"

    user_me_response = requests.get(url=base_api_url + path, 
                                 headers={'Authorization': access_token['Authorization']})
    
    json_user_me_data = user_me_response.json()

    assert user_me_response.status_code == 200
    assert credentials['username'] == json_user_me_data['username']


def test_change_user_data(base_api_url, access_token, credentials):
    path = "/api/v1/profile/"

    json_user_me_data = requests.get(url=base_api_url + "/api/v1/auth/users/me/", 
                                 headers={'Authorization': access_token['Authorization']}).json()

    changed_name = json_user_me_data['first_name'] + 'CHANGED'

    changed_user_data_response = requests.patch(url=base_api_url + path, 
                                 headers={'Authorization': access_token['Authorization']}, 
                                 json={'first_name': changed_name}).json()
    # json_changed_data = changed_user_data_response.json()

    print(changed_user_data_response['first_name'])

    # json_user_me_data = user_me_response.json()

    # assert user_me_response.status_code == 200
    # assert credentials['username'] == json_user_me_data['username']
