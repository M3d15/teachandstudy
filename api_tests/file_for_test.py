import random
from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()

category_list = [1,2,3,4,5]

random_category = random.choice(category_list)

print(type(random_category))