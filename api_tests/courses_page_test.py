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


def test_course_categories_list(base_api_url, access_token):
    path = "/api/v1/category/"

    course_categories_list_response = requests.get(url=base_api_url + path, 
                                 headers={'Authorization': access_token.get('Authorization')})
    
    assert course_categories_list_response.status_code == 200
    json_course_categories_data = course_categories_list_response.json()

    if len(json_course_categories_data) > 0:
        assert json_course_categories_data != []


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
    
    
def test_filter_courses_by_category(base_api_url, access_token):
    path = "/api/v1/courses/"

    course_categories_list_response = requests.get(url=base_api_url + "/api/v1/category/", 
                                 headers={'Authorization': access_token.get('Authorization')}).json()
    
    query_params = {
                    'limit': 16,
                    'page': 1
                    }
    
    if len(course_categories_list_response) > 0:
        for object in course_categories_list_response:
            if 'Сметное дело' in object.values():
                category_id = object.get('id')
                query_params = {
                    'limit': 16,
                    'page': 1,
                    'category': category_id
                    }
    
    filter_courses_by_category_response = requests.get(url=base_api_url + path, params=query_params,
                                 headers={'Authorization': access_token.get('Authorization')})
    
    assert filter_courses_by_category_response.status_code == 200
    json_filter_courses_by_category_data = filter_courses_by_category_response.json()
    assert json_filter_courses_by_category_data != {}
    
    if len(json_filter_courses_by_category_data.get('results')) > 0 and query_params.get('category') is not None:
        assert category_id in json_filter_courses_by_category_data.get('results')[0].get('category')
