import requests
import allure
# from ..api_tests.generator import random_name


@allure.story('Course view page')
@allure.title('Retrieve the course data')
def test_course_view(base_api_url, access_token):
    path = "/api/v1/courses/"
    with allure.step('Set query parameters'):
        query_params = {
            'limit': 16,
            'page': 1,
            }
        
    with allure.step('Retrieve the courses list from the API'):
        courses_list_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Retrieve the first course id'):
        first_course_id = courses_list_response.get('results')[0].get('id')

    with allure.step('Retrieve course data from the API'):
        course_view_response = requests.get(url=f"{base_api_url}{path}{first_course_id}/",
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'):
        assert course_view_response.status_code == 200
    json_course_view_data = course_view_response.json()

    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_course_view_data != {}

    with allure.step('Verify course data in the response'):
        with allure.step('Verify first_name'):
            assert json_course_view_data.get('id')
        with allure.step('Verify first_name'):
            assert json_course_view_data.get('name')
        with allure.step('Verify last_name with one in the response'):
            assert json_course_view_data.get('is_public') is True


@allure.story('Course view page')
@allure.title('Retrieve the recommended courses list')
def test_recommended_courses_list(base_api_url, access_token):
    path = "/api/v1/courses/"
    with allure.step('Set query parameters'):
        query_params = {
            'limit': 16,
            'page': 1,
            }
        
    with allure.step('Retrieve the courses list from the API'):
        courses_list_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    if len(courses_list_response.get('results')) > 0:
        with allure.step('Retrieve the first course category'):
            first_course_category = courses_list_response.get('results')[0].get('category')[0]
        
        with allure.step('Set query parameters with category'):
            query_params = {
                'limit': 4,
                'page': 1,
                'category': first_course_category
                }
            
        with allure.step('Retrieve the recommended courses list from the API by category'):
            recommended_courses_list_response = requests.get(url=base_api_url + path + 'recommended/', params=query_params,
                                        headers={'Authorization': access_token.get('Authorization')})
            
        with allure.step('Check the 200 status response'):
            assert recommended_courses_list_response.status_code == 200
        json_recommended_courses_list_data = recommended_courses_list_response.json()

        with allure.step('Check whether the dictionary isnt blank in the response'):
            assert recommended_courses_list_response != {}

        with allure.step('Check whether courses number more than 0'):
            if len(json_recommended_courses_list_data.get('results')) > 0:
                with allure.step('Verify the category of the first course'):
                    assert first_course_category in json_recommended_courses_list_data.get('results')[0].get('category')
                with allure.step('Verify the category of the last course'):
                    assert first_course_category in json_recommended_courses_list_data.get('results')[-1].get('category')
    