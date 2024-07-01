import random
from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()



def random_name():
    # Determine if the patronymic should be male or female
    gender = random.choice(['male', 'female'])

    # Generate the patronymic based on the gender
    if gender == 'male':
        male_patronymic_endings = ['ович', 'евич']
        patronymic = fake_ru.first_name_male() + random.choice(male_patronymic_endings)
        return {'first_name': fake_ru.first_name_male(), 'last_name': fake_ru.last_name_male(), 'patronymic': patronymic}
    else:
        female_patronymic_endings = ['овна', 'евна'] 
        patronymic = fake_ru.first_name_male() + random.choice(female_patronymic_endings)
        return {'first_name': fake_ru.first_name_female(), 'last_name': fake_ru.last_name_female(), 'patronymic': patronymic}
