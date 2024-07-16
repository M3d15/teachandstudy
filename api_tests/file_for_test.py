import random
from faker import Faker

fake_us = Faker('en_US')
fake_ru = Faker('ru_RU')
Faker.seed()

def generate_course_name():
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art', 'Music', 'Computer Science']
    course_types = ['Introduction to', 'Advanced', 'Basics of', 'Principles of', 'Fundamentals of', 'Theory of', 'Practical', 'Applications of']
    level = random.choice(['101', '201', '301', '401'])
    
    course_name = f"{random.choice(course_types)} {random.choice(subjects)} {level}"
    return course_name

# Generate and print 5 random course names
for _ in range(5):
    print(generate_course_name())