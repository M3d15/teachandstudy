import random
from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()

d = {}

d['name'] = 'Ivan'
d['surname'] = 'Petrov'


for i in d.items():
    key, value = i
    print(f'{key} = {value}')