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


@allure.story('Professions list page')
@allure.title('Profession view')
def test_profession_view(base_api_url, access_token):
    path = "/api/v1/professions/"
    
    with allure.step('Set query parameters'):
        query_params = {
            'page': 1,
            }

    with allure.step('Retrieve the professions list from the API'):
        professions_list_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Check whether professions number more than 0'):
        if len(professions_list_response) > 0:
            with allure.step('Get random number of the maximum number of professions in the list'):
                random_number = random.randrange(len(professions_list_response.get('results')))
            with allure.step('Retrieve teacher id from the random profession'):
                profession_id = professions_list_response.get('results')[random_number].get('id')
            with allure.step('Retrieve name of the random profession'):
                profession_name = professions_list_response.get('results')[random_number].get('name')
            with allure.step('Retrieve price of the random profession'):
                profession_price = professions_list_response.get('results')[random_number].get('price')
    
    with allure.step('Retrieve the profession data from the API'):
        profession_view_response = requests.get(url=f"{base_api_url}{path}{profession_id}/",
                                    headers={'Authorization': access_token.get('Authorization')})
    json_profession_view_data = profession_view_response.json()
    
    with allure.step('Check the 200 status response'):
        assert profession_view_response.status_code == 200
    
    with allure.step('Check whether the list isnt blank in the response'):
        assert json_profession_view_data != {}
    
    with allure.step('Verify profession data in the response'):
        with allure.step('Verify profession id'):
            assert json_profession_view_data.get('id') == profession_id
        
        with allure.step('Verify profession name'):
            assert json_profession_view_data.get('name') == profession_name
                
        with allure.step('Verify profession price'):
            assert json_profession_view_data.get('price') == profession_price
