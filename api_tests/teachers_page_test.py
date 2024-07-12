import requests
import allure
import random
# from ..api_tests.generator import random_name


@allure.story('Teachers list page')
@allure.title('Retrieve the teachers list')
def test_teachers_list(base_api_url, access_token):
    path = "/api/v1/teachers/"

    with allure.step('Set query parameters'):
        query_params = {
            'page': 1,
            }

    with allure.step('Retrieve the teachers list from the API'):
        teachers_list_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'):
        assert teachers_list_response.status_code == 200
    json_teachers_data = teachers_list_response.json()

    with allure.step('Check whether the list isnt blank in the response'):
        assert json_teachers_data != {}
    
    with allure.step('Check whether teachers number more than 0'):
        if len(json_teachers_data) > 0:
            with allure.step('Verify teachers data in the response'):
                with allure.step('Verify id of the first teacher'):
                    assert json_teachers_data.get('results')[0].get('id')
                with allure.step('Verify id of the last teacher'):
                    assert json_teachers_data.get('results')[-1].get('id')
                
                with allure.step('Verify first_name of the first teacher'):
                    assert json_teachers_data.get('results')[0].get('first_name')
                with allure.step('Verify first_name of the last teacher'):
                    assert json_teachers_data.get('results')[-1].get('first_name')
                
                with allure.step('Verify last_name of the first teacher'):
                    assert json_teachers_data.get('results')[0].get('last_name')
                with allure.step('Verify last_name of the last teacher'):
                    assert json_teachers_data.get('results')[-1].get('last_name')


@allure.story('Teachers list page')
@allure.title('Teachers search by name')
def test_teachers_search_by_name(base_api_url, access_token):
    path = "/api/v1/teachers/"
    
    with allure.step('Retrieve the teachers list from the API'):
        teachers_list_response = requests.get(url=base_api_url + path,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check whether teachers number more than 0'):
        if len(teachers_list_response) > 0:
            with allure.step('Get random number of the maximum number of teachers in the list'):
                random_number = random.randrange(len(teachers_list_response.get('results')))
            with allure.step('Retrieve first_name of the random teacher'):
                teachers_name = teachers_list_response.get('results')[random_number].get('first_name')
    
    with allure.step('Set query parameters'):
        query_params = {
            'page': 1,
            'search': teachers_name
            }
        
    with allure.step('Retrieve the teachers search result from the API'):
        teachers_search_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    json_teachers_search_data = teachers_search_response.json()
        
    with allure.step('Check the 200 status response'):
        assert teachers_search_response.status_code == 200
    
    with allure.step('Check whether the list isnt blank in the response'):
        assert json_teachers_search_data != {}
    
    with allure.step('Check whether teachers number more than 0'):
        if len(json_teachers_search_data.get('results')) > 0:
            with allure.step('Verify teachers data in the response'):
                with allure.step('Verify teachers first_name'):
                    assert json_teachers_search_data.get('results')[0].get('first_name') == teachers_name


@allure.story('Teachers list page')
@allure.title('Teachers search by last_name')
def test_teachers_search_by_last_name(base_api_url, access_token):
    path = "/api/v1/teachers/"
    
    with allure.step('Retrieve the teachers list from the API'):
        teachers_list_response = requests.get(url=base_api_url + path,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check whether teachers number more than 0'):
        if len(teachers_list_response) > 0:
            with allure.step('Get random number of the maximum number of teachers in the list'):
                random_number = random.randrange(len(teachers_list_response.get('results')))
            with allure.step('Retrieve last_name of the random teacher'):
                teachers_last_name = teachers_list_response.get('results')[random_number].get('last_name')
    
    with allure.step('Set query parameters'):
        query_params = {
            'page': 1,
            'search': teachers_last_name
            }
        
    with allure.step('Retrieve the teachers search result from the API'):
        teachers_search_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    json_teachers_search_data = teachers_search_response.json()
        
    with allure.step('Check the 200 status response'):
        assert teachers_search_response.status_code == 200
    
    with allure.step('Check whether the list isnt blank in the response'):
        assert json_teachers_search_data != {}
    
    with allure.step('Check whether teachers number more than 0'):
        if len(json_teachers_search_data.get('results')) > 0:
            with allure.step('Verify teachers data in the response'):
                with allure.step('Verify teachers last_name'):
                    assert json_teachers_search_data.get('results')[0].get('last_name') == teachers_last_name


@allure.story('Teachers list page')
@allure.title('Teachers search by patronymic')
def test_teachers_search_by_patronymic(base_api_url, access_token):
    path = "/api/v1/teachers/"
    
    with allure.step('Retrieve the teachers list from the API'):
        teachers_list_response = requests.get(url=base_api_url + path,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check whether teachers number more than 0'):
        if len(teachers_list_response) > 0:
            with allure.step('Look for a teacher with patronymic'):
                for data in teachers_list_response.get('results'):
                    if data.get('patronymic'):
                        patronymic = data.get('patronymic')
                        break

    if patronymic:
        with allure.step('Set query parameters'):
            query_params = {
                'page': 1,
                'search': patronymic
                }
            
        with allure.step('Retrieve the teachers search result from the API'):
            teachers_search_response = requests.get(url=base_api_url + path, params=query_params,
                                        headers={'Authorization': access_token.get('Authorization')})
        json_teachers_search_data = teachers_search_response.json()
            
        with allure.step('Check the 200 status response'):
            assert teachers_search_response.status_code == 200
        
        with allure.step('Check whether the list isnt blank in the response'):
            assert json_teachers_search_data != {}
        
        with allure.step('Check whether teachers number more than 0'):
            if len(json_teachers_search_data.get('results')) > 0:
                with allure.step('Verify teachers data in the response'):
                    with allure.step('Verify teachers patronymic'):
                        assert json_teachers_search_data.get('results')[0].get('patronymic') == patronymic
    else:
        print('There are no people with a patronymic here')


@allure.story('Teachers list page')
@allure.title('Teachers view')
def test_teachers_view(base_api_url, access_token):
    path = "/api/v1/teachers/"
    
    with allure.step('Retrieve the teachers list from the API'):
        teachers_list_response = requests.get(url=base_api_url + path,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check whether teachers number more than 0'):
        if len(teachers_list_response) > 0:
            with allure.step('Get random number of the maximum number teacher in the list'):
                random_number = random.randrange(len(teachers_list_response.get('results')))
            with allure.step('Retrieve teacher id from the random teacher'):
                teacher_id = teachers_list_response.get('results')[random_number].get('id')
            with allure.step('Retrieve first_name of the random teacher'):
                teacher_first_name = teachers_list_response.get('results')[random_number].get('first_name')
            with allure.step('Retrieve last_name of the random teacher'):
                teacher_last_name = teachers_list_response.get('results')[random_number].get('last_name')
            with allure.step('Check whether teacher has patronymic'):
                if teachers_list_response.get('results')[random_number].get('patronymic'):
                    with allure.step('Retrieve patronymic of the random teacher'):
                        patronymic = teachers_list_response.get('results')[random_number].get('patronymic')
    
    with allure.step('Retrieve the teachers data from the API'):
        teachers_view_response = requests.get(url=f"{base_api_url}{path}{teacher_id}/",
                                    headers={'Authorization': access_token.get('Authorization')})
    json_teachers_view_data = teachers_view_response.json()
    
    with allure.step('Check the 200 status response'):
        assert teachers_view_response.status_code == 200
    
    with allure.step('Check whether the list isnt blank in the response'):
        assert json_teachers_view_data != {}
    
    with allure.step('Verify teachers data in the response'):
        with allure.step('Verify teachers id'):
            assert json_teachers_view_data.get('id') == teacher_id
        
        with allure.step('Verify teachers first_name'):
                    assert json_teachers_view_data.get('first_name') == teacher_first_name
                
        with allure.step('Verify teachers last_name'):
            assert json_teachers_view_data.get('last_name') == teacher_last_name

        with allure.step('Check whether teacher has patronymic'):
            if json_teachers_view_data.get('patronymic'):
                with allure.step('Verify teachers patronymic'):
                    assert json_teachers_view_data.get('patronymic') == patronymic