import requests
# from ..api_tests.generator import random_name

def test_courses_list(base_api_url, access_token, credentials):
    courses_number = 16
    path = f"/api/v1/courses/?limit={courses_number}&page=1"

    courses_list_response = requests.get(url=base_api_url + path, 
                                 headers={'Authorization': access_token['Authorization']})
    
    assert courses_list_response.status_code == 200
    json_courses_list_data = courses_list_response.json()

    if int(json_courses_list_data['count']) >= courses_number:
        assert len(json_courses_list_data['results']) == courses_number
        