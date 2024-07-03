import requests
# from ..api_tests.generator import random_name

def test_courses_list(base_api_url, access_token):
    courses_number = 16
    path = f"/api/v1/courses/?limit={courses_number}&page=1"

    courses_list_response = requests.get(url=base_api_url + path, 
                                 headers={'Authorization': access_token.get('Authorization')})
    
    assert courses_list_response.status_code == 200
    json_courses_list_data = courses_list_response.json()

    if int(json_courses_list_data.get('count')) >= courses_number:
        assert len(json_courses_list_data.get('results')) == courses_number


def test_courses_search(base_api_url, access_token):
    path = "/api/v1/courses/"

    json_courses_list_data = requests.get(url=base_api_url + path, 
                                 headers={'Authorization': access_token.get('Authorization')}).json()
    first_course_name = json_courses_list_data.get('results')[0].get('name')
    
    query_params = {
        'limit': 16,
        'page': 1,
        'search': first_course_name,
        }
    
    course_search_response = requests.get(url=base_api_url + path, params=query_params,
                                 headers={'Authorization': access_token.get('Authorization')})
    
    assert course_search_response.status_code == 200
    json_course_search_data = course_search_response.json()
    
    if len(json_course_search_data.get('results')) > 0:
        assert json_course_search_data.get('results')[0].get('name') == first_course_name
    
    

        