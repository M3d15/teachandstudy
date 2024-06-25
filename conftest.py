import pytest
import requests


@pytest.fixture()
def credentials():
    return {"username": "test@ya.ru", "password": "1qwe2qaz"}


@pytest.fixture()
def access_token(base_api_url, credentials):
    path = "/api/v1/auth/jwt/create/"
    token_response = requests.post(url=base_api_url + path, json=credentials,
                         verify=False)
    
    assert token_response.status_code == 200
    json_token_data = token_response.json()
    
    return {"Authorization": f"Bearer {json_token_data['access']}"}


@pytest.fixture()
def base_api_url():
    return "https://tastest.pelikan.online"
