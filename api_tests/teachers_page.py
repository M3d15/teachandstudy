import requests
import allure
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