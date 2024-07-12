import requests
import allure
import random
# from ..api_tests.generator import random_name


@allure.story('Professions list page')
@allure.title('Retrieve the professions list')
def test_professions_list(base_api_url, access_token):
    path = "/api/v1/professions/"

    with allure.step('Set query parameters'):
        query_params = {
            'page': 1,
            }

    with allure.step('Retrieve the professions list from the API'):
        professions_list_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'):
        assert professions_list_response.status_code == 200
    json_professions_data = professions_list_response.json()

    with allure.step('Check whether the list isnt blank in the response'):
        assert json_professions_data != {}
    
    with allure.step('Check whether professions number more than 0'):
        if len(json_professions_data) > 0:
            with allure.step('Verify professions data in the response'):
                with allure.step('Verify id of the first profession'):
                    assert json_professions_data.get('results')[0].get('id')
                with allure.step('Verify id of the last profession'):
                    assert json_professions_data.get('results')[-1].get('id')
                
                with allure.step('Verify name of the first profession'):
                    assert json_professions_data.get('results')[0].get('name')
                with allure.step('Verify name of the last profession'):
                    assert json_professions_data.get('results')[-1].get('name')
                
                with allure.step('Verify price of the first profession'):
                    assert json_professions_data.get('results')[0].get('price')
                with allure.step('Verify price of the last profession'):
                    assert json_professions_data.get('results')[-1].get('price')
