from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()


# class Gen:
#     def random_name():
#         return {'first_name': fake_ru.first_name(), 'last_name': fake_ru.last_name()}

def random_name():
    return "John Doe"

class Gen:
    def __init__(self):
        self.name = random_name()