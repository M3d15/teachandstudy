import random
from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()

lst = [7]
response_list = [1]

if response_list[0] in lst:
    print('true')
else:
    print('false')