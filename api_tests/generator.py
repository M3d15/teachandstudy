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
        return {'first_name': fake_ru.first_name_male(), 'last_name': fake_ru.last_name_male(), 'patronymic': patronymic, 'phone': fake_ru.phone_number()}
    else:
        female_patronymic_endings = ['овна', 'евна'] 
        patronymic = fake_ru.first_name_male() + random.choice(female_patronymic_endings)
        return {'first_name': fake_ru.first_name_female(), 'last_name': fake_ru.last_name_female(), 'patronymic': patronymic, 'phone': fake_ru.phone_number()}
    
def generate_course_name():
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art', 'Music', 'Computer Science']
    course_types = ['Introduction to', 'Advanced', 'Basics of', 'Principles of', 'Fundamentals of', 'Theory of', 'Practical', 'Applications of']
    level = random.choice(['101', '201', '301', '401'])
    
    course_name = f"{random.choice(course_types)} {random.choice(subjects)} {level}"
    return course_name
