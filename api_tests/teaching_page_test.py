import requests
import allure
import random
import pytest
from ..api_tests.generator import generate_course_name


@allure.story('Teaching page')
@allure.title('Free course creating')
def test_create_free_course(base_api_url, access_token):
    path = "/api/v1/teaching/courses/"
    category_list = []

    with allure.step('Retrieve users data from the API'):
        json_user_me_data = requests.get(url=base_api_url + "/api/v1/auth/users/me/", 
                                    headers={'Authorization': access_token.get('Authorization')}).json()

    with allure.step('Retrieve the courses categories list from the API'):
        json_course_categories_list_data = requests.get(url=base_api_url + '/api/v1/category/', 
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check if categories number > 0'):
        if len(json_course_categories_list_data) > 0:
            with allure.step('Getting category ids from the response'):
                for object in json_course_categories_list_data:
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
                    assert json_course_creating_data.get('category') == body.get('category')


@allure.story('Teaching page')
@allure.title('Course editing')
def test_edit_course(base_api_url, access_token):
    category_list = []

    with allure.step('Set query parameters for user courses list'):
        query_params = {
            'limit': 12,
            'page': 1,
            }
    with allure.step('Retrieve course list'):
        json_course_list_data = requests.get(url=base_api_url + '/api/v1/courses/teacher/', params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check if courses number > 0'):
        if len(json_course_list_data.get('results')) > 0:
            with allure.step('Retrieve users data from the API'):
                json_user_me_data = requests.get(url=base_api_url + "/api/v1/auth/users/me/", 
                                            headers={'Authorization': access_token.get('Authorization')}).json()

            with allure.step('Retrieve the courses categories list from the API'):
                json_course_categories_list_data = requests.get(url=base_api_url + '/api/v1/category/', 
                                            headers={'Authorization': access_token.get('Authorization')}).json()
            
            with allure.step('Check if categories number > 0'):
                if len(json_course_categories_list_data) > 0:
                    with allure.step('Getting category ids from the response'):
                        for object in json_course_categories_list_data:
                            category_list.append(object.get('id'))
                            if len(category_list) >= 10:
                                break
                    
                    path = f"/api/v1/teaching/courses/{json_course_list_data.get('results')[-1].get('id')}/"

                    with allure.step('Set query parameters for course editing'):
                        body = {
                            'name': f'{generate_course_name()}',
                            'certificate_scores': random.randint(1, 100),
                            'academic_hours': random.randint(1, 200),
                            'category': [],
                            'price': 0,
                            'description': f'some course description 123 !@# {generate_course_name()}',
                            'teachers': [json_user_me_data.get('id')],
                            'is_enabled_questions': False,
                            'is_active_referral': False
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
                            assert json_course_editing_data.get('id') == json_course_list_data.get('results')[-1].get('id')
                        with allure.step('Verify changed course name'):
                            assert json_course_editing_data.get('name') == body.get('name')
                        with allure.step('Verify changed course certificate scores'):
                            assert json_course_editing_data.get('certificate_scores') == body.get('certificate_scores')
                        with allure.step('Verify changed course academic hours'):
                            assert json_course_editing_data.get('academic_hours') == body.get('academic_hours')
                        with allure.step('Verify teacher id'):
                            assert json_course_editing_data.get('teachers')[0] == body.get('teachers')[0]
                        with allure.step('Verify course status'):
                            assert json_course_editing_data.get('status') == 'NEW'
                        with allure.step('Verify changed course category'):
                            assert json_course_editing_data.get('category') == []
        else:
            pytest.fail("There is no courses to edit")


@allure.story('Teaching page')
@allure.title('Phys paid course creating')
def test_create_phys_paid_course(base_api_url, access_token):
    path = "/api/v1/teaching/courses/"
    category_list = []

    with allure.step('Retrieve users data from the API'):
        json_user_me_data = requests.get(url=base_api_url + "/api/v1/auth/users/me/", 
                                    headers={'Authorization': access_token.get('Authorization')}).json()

    with allure.step('Retrieve the courses categories list from the API'):
        json_course_categories_list_data = requests.get(url=base_api_url + '/api/v1/category/', 
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check if categories number > 0'):
        if len(json_course_categories_list_data) > 0:
            with allure.step('Getting category ids from the response'):
                for object in json_course_categories_list_data:
                    category_list.append(object.get('id'))
                    if len(category_list) >= 10:
                        break
        
            with allure.step('Set query parameters'):
                body = {
                    'name': f'{generate_course_name()} for physical people',
                    'category': [random.choice(category_list)],
                    'certificate_scores': random.randint(1, 100),
                    'academic_hours': random.randint(1, 200),
                    'price': random.randint(1, 2147483647),
                    'price_discount': 1,
                    'description': 'some paid course description 123 !@#',
                    'is_enabled_questions': True,
                    'is_active_referral': True,
                    'teachers': [json_user_me_data.get('id')],
                    'requisite.type': 'PRS',
                    'requisite.fio': f'{json_user_me_data.get('first_name')} {json_user_me_data.get('last_name')}',
                    'requisite.account': '12345678901234567890',
                    'requisite.inn': '9103014604',
                    'requisite.bik': '123456789',
                    'requisite.passport': '2488 145533'
                    }
            
            with allure.step('Course creating'):
                course_creating_response = requests.post(url=base_api_url + path, data=body,
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
                    assert json_course_creating_data.get('category') == body.get('category')
            
            with allure.step('Verify course requisites data in the response'):
                with allure.step('Verify course requisites type'):
                    assert json_course_creating_data.get('requisite').get('type') == body.get('requisite.type')
                with allure.step('Verify user fio'):
                    assert json_course_creating_data.get('requisite').get('fio') == body.get('requisite.fio')
                with allure.step('Verify course requisites account'):
                    assert json_course_creating_data.get('requisite').get('account') == body.get('requisite.account')
                with allure.step('Verify course requisites inn'):
                    assert json_course_creating_data.get('requisite').get('inn') == body.get('requisite.inn')
                with allure.step('Verify course requisites bik'):
                    assert json_course_creating_data.get('requisite').get('bik') == body.get('requisite.bik')
                with allure.step('Verify course requisites passport'):
                    assert json_course_creating_data.get('requisite').get('passport') == body.get('requisite.passport')


@allure.story('Teaching page')
@allure.title('Self-employed paid course creating')
def test_create_phys_slf_empld_paid_course(base_api_url, access_token):
    path = "/api/v1/teaching/courses/"
    category_list = []

    with allure.step('Retrieve users data from the API'):
        json_user_me_data = requests.get(url=base_api_url + "/api/v1/auth/users/me/", 
                                    headers={'Authorization': access_token.get('Authorization')}).json()

    with allure.step('Retrieve the courses categories list from the API'):
        json_course_categories_list_data = requests.get(url=base_api_url + '/api/v1/category/', 
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check if categories number > 0'):
        if len(json_course_categories_list_data) > 0:
            with allure.step('Getting category ids from the response'):
                for object in json_course_categories_list_data:
                    category_list.append(object.get('id'))
                    if len(category_list) >= 10:
                        break
        
            with allure.step('Set query parameters'):
                body = {
                    'name': f'{generate_course_name()} for self-employed people',
                    'category': [random.choice(category_list)],
                    'certificate_scores': random.randint(1, 100),
                    'academic_hours': random.randint(1, 200),
                    'price': random.randint(1, 2147483647),
                    'price_discount': 1,
                    'description': 'some paid course description 123 !@#',
                    'is_enabled_questions': True,
                    'is_active_referral': True,
                    'teachers': [json_user_me_data.get('id')],
                    'requisite.type': 'SLF',
                    'requisite.fio': f'{json_user_me_data.get('first_name')} {json_user_me_data.get('last_name')}',
                    'requisite.account': '12345678901234567890',
                    'requisite.inn': '9103014604',
                    'requisite.bik': '123456789',
                    'requisite.passport': '2488 145533'
                    }
            
            with allure.step('Course creating'):
                course_creating_response = requests.post(url=base_api_url + path, data=body,
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
                    assert json_course_creating_data.get('category') == body.get('category')
            
            with allure.step('Verify course requisites data in the response'):
                with allure.step('Verify course requisites type'):
                    assert json_course_creating_data.get('requisite').get('type') == body.get('requisite.type')
                with allure.step('Verify user fio'):
                    assert json_course_creating_data.get('requisite').get('fio') == body.get('requisite.fio')
                with allure.step('Verify course requisites account'):
                    assert json_course_creating_data.get('requisite').get('account') == body.get('requisite.account')
                with allure.step('Verify course requisites inn'):
                    assert json_course_creating_data.get('requisite').get('inn') == body.get('requisite.inn')
                with allure.step('Verify course requisites bik'):
                    assert json_course_creating_data.get('requisite').get('bik') == body.get('requisite.bik')
                with allure.step('Verify course requisites passport'):
                    assert json_course_creating_data.get('requisite').get('passport') == body.get('requisite.passport')


@allure.story('Teaching page')
@allure.title('Individual entrepreneur paid course creating')
def test_create_ie_paid_course(base_api_url, access_token):
    path = "/api/v1/teaching/courses/"
    category_list = []

    with allure.step('Retrieve users data from the API'):
        json_user_me_data = requests.get(url=base_api_url + "/api/v1/auth/users/me/", 
                                    headers={'Authorization': access_token.get('Authorization')}).json()

    with allure.step('Retrieve the courses categories list from the API'):
        json_course_categories_list_data = requests.get(url=base_api_url + '/api/v1/category/', 
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check if categories number > 0'):
        if len(json_course_categories_list_data) > 0:
            with allure.step('Getting category ids from the response'):
                for object in json_course_categories_list_data:
                    category_list.append(object.get('id'))
                    if len(category_list) >= 10:
                        break
        
            with allure.step('Set query parameters'):
                body = {
                    'name': f'{generate_course_name()} for individual entrepreneurs',
                    'category': [random.choice(category_list)],
                    'certificate_scores': random.randint(1, 100),
                    'academic_hours': random.randint(1, 200),
                    'price': random.randint(1, 2147483647),
                    'price_discount': 1,
                    'description': 'some paid course description 123 !@#',
                    'is_enabled_questions': True,
                    'is_active_referral': True,
                    'teachers': [json_user_me_data.get('id')],
                    'requisite.type': 'IND',
                    'requisite.fio': f'{json_user_me_data.get('first_name')} {json_user_me_data.get('last_name')}',
                    'requisite.account': '12345678901234567890',
                    'requisite.inn': '910311329511',
                    'requisite.bik': '123456789',
                    'requisite.nds': random.randint(0, 20)
                    }
            
            with allure.step('Course creating'):
                course_creating_response = requests.post(url=base_api_url + path, data=body,
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
                    assert json_course_creating_data.get('category') == body.get('category')
            
            with allure.step('Verify course requisites data in the response'):
                with allure.step('Verify course requisites type'):
                    assert json_course_creating_data.get('requisite').get('type') == body.get('requisite.type')
                with allure.step('Verify user fio'):
                    assert json_course_creating_data.get('requisite').get('fio') == body.get('requisite.fio')
                with allure.step('Verify course requisites account'):
                    assert json_course_creating_data.get('requisite').get('account') == body.get('requisite.account')
                with allure.step('Verify course requisites inn'):
                    assert json_course_creating_data.get('requisite').get('inn') == body.get('requisite.inn')
                with allure.step('Verify course requisites bik'):
                    assert json_course_creating_data.get('requisite').get('bik') == body.get('requisite.bik')
                with allure.step('Verify course requisites nds'):
                    assert json_course_creating_data.get('requisite').get('nds') == body.get('requisite.nds')