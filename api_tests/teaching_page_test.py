import requests
import allure
import random
from ..api_tests.generator import generate_course_name


@allure.story('Teaching page')
@allure.title('Course creating')
def test_create_free_course(base_api_url, access_token):
    path = "/api/v1/courses/"
    category_list = []

    with allure.step('Retrieve users data from the API'):
        json_user_me_data = requests.get(url=base_api_url + "/api/v1/auth/users/me/", 
                                    headers={'Authorization': access_token.get('Authorization')}).json()

    with allure.step('Retrieve the courses categories list from the API'):
        course_categories_list_response = requests.get(url=base_api_url + '/api/v1/category/', 
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check if categories number > 0'):
        if len(course_categories_list_response) > 0:
            with allure.step('Getting category ids from the response'):
                for object in course_categories_list_response:
                    category_list.append(object.get('id'))
                    if len(category_list) >= 10:
                        break

            with allure.step('Set query parameters'):
                body = {
                    'name': f'{generate_course_name()}',
                    'category': [random.choice(category_list)],
                    'certificate_scores': random.randint(1, 100),
                    'academic_hours': random.randint(1, 200),
                    'price': 0,
                    'description': 'some course description 123 !@#',
                    'is_enabled_questions': False,
                    'is_active_referral': False,
                    'teachers': [json_user_me_data.get('id')]
                    }

            with allure.step('Course creating'):
                course_creating_response = requests.post(url=base_api_url + path, json=body,
                                            headers={'Authorization': access_token.get('Authorization')})
            
            with allure.step('Check the 201 status response'):
                assert course_creating_response.status_code == 201
            json_course_creating_data = course_creating_response.json()

            with allure.step('Check whether the list isnt blank in the response'):
                assert json_course_creating_data != {}
            
            with allure.step('Verify course data in the response'):
                with allure.step('Verify course name'):
                    assert json_course_creating_data.get('name') == body.get('name')
                with allure.step('Verify course certificate scores'):
                    assert json_course_creating_data.get('certificate_scores') == body.get('certificate_scores')
                with allure.step('Verify course academic hours'):
                    assert json_course_creating_data.get('academic_hours') == body.get('academic_hours')
                with allure.step('Verify teacher id'):
                    assert json_course_creating_data.get('teachers')[0] == body.get('teachers')[0]
                with allure.step('Verify course status'):
                    assert json_course_creating_data.get('status') == 'NEW'
                with allure.step('Verify course category'):
                    assert body.get('category')[0] in json_course_creating_data.get('category')


@allure.story('Teaching page')
@allure.title('Course editing')
def test_edit_course(base_api_url, access_token):
    with allure.step('Set query parameters'):
        query_params = {
            'limit': 16,
            'page': 1,
            }
    
    with allure.step('Retrieve course list'):
        course_list_response = requests.get(url=base_api_url + '/api/v1/courses/teacher/', params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    path = f"/api/v1/courses/{course_list_response.get('results')[-1].get('id')}/"

    with allure.step('Set query parameters'):
        body = {
            'name': 'course 3CHANGED',
            'category': []
            }

    with allure.step('Course editing'):
        course_editing_response = requests.put(url=base_api_url + path, json=body,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'):
        assert course_editing_response.status_code == 200
    json_course_editing_data = course_editing_response.json()

    with allure.step('Check whether the list isnt blank in the response'):
        assert json_course_editing_data != {}
    
    
    with allure.step('Verify course data in the response'):
        with allure.step('Verify course id'):
            assert json_course_editing_data.get('id') == course_list_response.get('results')[-1].get('id')
        with allure.step('Verify changed course name'):
            assert json_course_editing_data.get('name') == body.get('name')
        with allure.step('Verify changed course category'):
            assert json_course_editing_data.get('category') == []


