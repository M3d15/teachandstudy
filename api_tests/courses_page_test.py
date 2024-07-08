import requests
import allure
# from ..api_tests.generator import random_name


@allure.story('Courses list page')
@allure.title('Retrieve the courses list')
def test_courses_list(base_api_url, access_token):
    courses_number = 16
    path = f"/api/v1/courses/?limit={courses_number}&page=1"

    with allure.step('Retrieve the courses list from the API'):
        courses_list_response = requests.get(url=base_api_url + path, 
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'):
        assert courses_list_response.status_code == 200
    json_courses_list_data = courses_list_response.json()

    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_courses_list_data != {}

    if int(json_courses_list_data.get('count')) >= courses_number:
        with allure.step('Check whether courses number correspond with provided number'):
            assert len(json_courses_list_data.get('results')) == courses_number


@allure.story('Courses list page')
@allure.title('Retrieve the courses categories list')
def test_course_categories_list(base_api_url, access_token):
    path = "/api/v1/category/"

    with allure.step('Retrieve the courses categories list from the API'):
        course_categories_list_response = requests.get(url=base_api_url + path, 
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'):  
        assert course_categories_list_response.status_code == 200
    json_course_categories_data = course_categories_list_response.json()

    if len(json_course_categories_data) > 0:
        with allure.step('Check whether the list isnt blank in the response'):
            assert json_course_categories_data != []


@allure.story('Courses list page')
@allure.title('Course search')
def test_courses_search(base_api_url, access_token):
    path = "/api/v1/courses/"

    with allure.step('Retrieve the courses list from the API'):
        json_courses_list_data = requests.get(url=base_api_url + path, 
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    if int(json_courses_list_data.get('count')) > 0:
        with allure.step('Retrieve the first course name'):
            first_course_name = json_courses_list_data.get('results')[0].get('name')
    
        with allure.step('Set query parameters with the course name'):
            query_params = {
                'limit': 16,
                'page': 1,
                'search': first_course_name,
                }
        
        with allure.step('Get search results from the API'):
            course_search_response = requests.get(url=base_api_url + path, params=query_params,
                                        headers={'Authorization': access_token.get('Authorization')})
        
        with allure.step('Check the 200 status response'):  
            assert course_search_response.status_code == 200
        json_course_search_data = course_search_response.json()
        
        with allure.step('Verify provided course name with one in the response'):  
            assert json_course_search_data.get('results')[0].get('name') == first_course_name
    else:
        print('Courses list is empty')


@allure.story('Courses list page')
@allure.title('Sort courses by rating')
def test_sort_courses_by_rating(base_api_url, access_token):
    path = "/api/v1/courses/"
        
    with allure.step('Set query parameters with sort rating'):
        query_params = {
            'limit': 16,
            'page': 1,
            'ordering': 'rating'
            }
    
    with allure.step('Retrieve the sorted courses list from the API'):
        sorted_courses_by_category_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'): 
        assert sorted_courses_by_category_response.status_code == 200
    json_sorted_courses_by_category_data = sorted_courses_by_category_response.json()
    
    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_sorted_courses_by_category_data != {}
    
    if len(json_sorted_courses_by_category_data.get('results')) > 1 and json_sorted_courses_by_category_data.get('results')[-1].get('review_score') is not None:
        first_course_rating = json_sorted_courses_by_category_data.get('results')[0].get('review_score')
        last_course_rating = json_sorted_courses_by_category_data.get('results')[-1].get('review_score')
        
        with allure.step('Comparison rating of first and last courses'):
            assert first_course_rating >= last_course_rating


@allure.story('Courses list page')
@allure.title('Sort courses by popular')
def test_sort_courses_by_popular(base_api_url, access_token):
    path = "/api/v1/courses/"
        
    with allure.step('Set query parameters with sort popular'):
        query_params = {
            'limit': 16,
            'page': 1,
            'ordering': 'popular'
            }
    
    with allure.step('Retrieve the sorted courses list from the API'):
        sorted_courses_by_category_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'): 
        assert sorted_courses_by_category_response.status_code == 200
    json_sorted_courses_by_category_data = sorted_courses_by_category_response.json()
    
    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_sorted_courses_by_category_data != {}


@allure.story('Courses list page')
@allure.title('Filter courses by category')
def test_filter_courses_by_category(base_api_url, access_token):
    path = "/api/v1/courses/"

    with allure.step('Retrieve the courses categories list from the API'):
        course_categories_list_response = requests.get(url=base_api_url + "/api/v1/category/", 
                                    headers={'Authorization': access_token.get('Authorization')}).json()
    
    with allure.step('Set base query parameters'):
        query_params = {
                        'limit': 16,
                        'page': 1
                        }
        
    with allure.step('Set query parameters with category id'):
        if len(course_categories_list_response) > 0:
            for object in course_categories_list_response:
                if 'Сметное дело' in object.values():
                    category_id = object.get('id')
                    query_params = {
                        'limit': 16,
                        'page': 1,
                        'category': category_id
                        }
    
    with allure.step('Retrieve the filtered courses list from the API'):
        filter_courses_by_category_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'): 
        assert filter_courses_by_category_response.status_code == 200
    json_filter_courses_by_category_data = filter_courses_by_category_response.json()
    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_filter_courses_by_category_data != {}
    
    if len(json_filter_courses_by_category_data.get('results')) > 0 and query_params.get('category') is not None:
        with allure.step('Verify provided category id with one in the response'):  
            assert category_id in json_filter_courses_by_category_data.get('results')[0].get('category')


@allure.story('Courses list page')
@allure.title('Filter courses by paid')
def test_filter_courses_by_paid(base_api_url, access_token):
    path = "/api/v1/courses/"
        
    with allure.step('Set query parameters with paid filter'):
        query_params = {
            'limit': 16,
            'page': 1,
            'price': 'paid'
            }
    
    with allure.step('Retrieve the filtered courses list from the API'):
        filtered_courses_by_paid_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'): 
        assert filtered_courses_by_paid_response.status_code == 200
    json_filtered_courses_data = filtered_courses_by_paid_response.json()
    
    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_filtered_courses_data != {}
    
    with allure.step('Check whether courses number more than 0'):
        if len(json_filtered_courses_data.get('results')) > 0:
            with allure.step('Verify the first course price'):
                assert json_filtered_courses_data.get('results')[0].get('price') > 0
            with allure.step('Verify the last course price'):
                assert json_filtered_courses_data.get('results')[-1].get('price') > 0


@allure.story('Courses list page')
@allure.title('Filter courses by free')
def test_filter_courses_by_free(base_api_url, access_token):
    path = "/api/v1/courses/"
        
    with allure.step('Set query parameters with free filter'):
        query_params = {
            'limit': 16,
            'page': 1,
            'price': 'free'
            }
    
    with allure.step('Retrieve the filtered courses list from the API'):
        filtered_courses_by_free_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'): 
        assert filtered_courses_by_free_response.status_code == 200
    json_filtered_courses_data = filtered_courses_by_free_response.json()
    
    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_filtered_courses_data != {}
    
    with allure.step('Check whether courses number more than 0'):
        if len(json_filtered_courses_data.get('results')) > 0:
            with allure.step('Verify the first course price'):
                assert json_filtered_courses_data.get('results')[0].get('price') == 0
            with allure.step('Verify the last course price'):
                assert json_filtered_courses_data.get('results')[-1].get('price') == 0


@allure.story('Courses list page')
@allure.title('Filter courses by referral')
def test_filter_courses_by_referral(base_api_url, access_token):
    path = "/api/v1/courses/"
        
    with allure.step('Set query parameters with referral filter'):
        query_params = {
            'limit': 16,
            'page': 1,
            'price': 'referral'
            }
    
    with allure.step('Retrieve the filtered courses list from the API'):
        filtered_courses_by_referral_response = requests.get(url=base_api_url + path, params=query_params,
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'): 
        assert filtered_courses_by_referral_response.status_code == 200
    json_filtered_courses_data = filtered_courses_by_referral_response.json()
    
    with allure.step('Check whether the dictionary isnt blank in the response'):
        assert json_filtered_courses_data != {}
    
    with allure.step('Check whether courses number more than 0'):
        if len(json_filtered_courses_data.get('results')) > 0:
            with allure.step('Verify the referral existance of the first course'):
                assert json_filtered_courses_data.get('results')[0].get('is_active_referral') is True
            with allure.step('Verify the referral existance of the first course'):
                assert json_filtered_courses_data.get('results')[-1].get('is_active_referral') is True


@allure.story('Courses list page')
@allure.title('Retrieve the top teachers list')
def test_teachers_list(base_api_url, access_token):
    path = "/api/v1/teachers/top-teachers/"

    with allure.step('Retrieve the teachers list from the API'):
        teachers_list_response = requests.get(url=base_api_url + path, 
                                    headers={'Authorization': access_token.get('Authorization')})
    
    with allure.step('Check the 200 status response'):
        assert teachers_list_response.status_code == 200
    json_teachers_data = teachers_list_response.json()

    if len(json_teachers_data) > 0:
        with allure.step('Check whether the list isnt blank in the response'):
            assert json_teachers_data != []

    with allure.step('Check whether teachers number more than 0'):
        if len(json_teachers_data) > 0:
            with allure.step('Verify teachers data in the response'):
                with allure.step('Verify first_name'):
                    assert json_teachers_data[0].get('id')
                with allure.step('Verify first_name'):
                    assert json_teachers_data[0].get('first_name')
                with allure.step('Verify last_name with one in the response'):
                    assert json_teachers_data[0].get('last_name')
        