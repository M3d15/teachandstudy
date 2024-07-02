import random
from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()

# def random_name():
#     male_patronymic_endings = ['ович', 'евич']
#     female_patronymic_endings = ['овна', 'евна']

#     # Determine if the patronymic should be male or female
#     gender = random.choice(['male', 'female'])

#     # Generate the patronymic based on the gender
#     if gender == 'male':
#         first_name = fake_ru.first_name_male()
#         last_name = fake_ru.last_name_male()
#         male_first_name = fake_ru.first_name_male()
#         random_choice_of = random.choice(male_patronymic_endings)
#         patronymic = male_first_name + random_choice_of
#         return {'first_name': first_name, 'last_name': last_name, 'patronymic': patronymic}
#     else:
#         first_name = fake_ru.first_name_female()
#         last_name = fake_ru.last_name_female()
#         patronymic = fake_ru.first_name_male() + random.choice(female_patronymic_endings)
#         return {'first_name': first_name, 'last_name': last_name, 'patronymic': patronymic}
        
phone_number = fake_ru.phone_number()

print(phone_number)

