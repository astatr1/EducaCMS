import requests

# Необходимо ввести логин/пароль пользователя
username = ''
password = ''
base_url = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}courses/')
courses = r.json()

available_courses = ', '.join([course['title'] for course in courses])
print(f'Доступные курсы: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}courses/{course_id}/enroll/',
                      auth=(username, password))
    if r.status_code == 200:
        print(f' Успешная запись на курс: {course_title}')
    else:
        print(f'Ошибка записи на курс по API. {r.status_code}')
