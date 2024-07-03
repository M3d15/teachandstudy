import random
from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()

course_categories_list_response = [{'id': 1, 'name': '123'}, {'id': 2, 'name': 'Сметное дело1'}]

query_params = {
            'limit': 16,
            'page': 1
            }

# for object in course_categories_list_response:
#     if 'Сметное дело' in object.values():
#         category_id = object.get('id')
#         query_params = {
#             'limit': 16,
#             'page': 1,
#             'category': category_id
#             }

if query_params.get('123') is None:
    print(query_params.get('123'))