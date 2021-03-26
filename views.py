from logging_mod import Logger
from models import TrainingSite
from my_framework import render, Application

# Создание копирование курса, список курсов
# Регистрация пользователя, список пользователей
# Логирование

site = TrainingSite()
LOGGER = Logger('main')


def main_view(request):
    my_key, my_title = request.get(
        'my_key', None), request.get('my_title', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', my_key=my_key, my_title=my_title)


def course_list_view(request):
    LOGGER.debug(f'Список курсов - {site.courses}')
    return '200 OK', render('course_list.html', objects_list=site.courses)


def create_course_view(request):
    if request['method'] == 'POST':
        # метод пост
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        # print(category_id)
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

            course = site.create_course('record', name, category)
            site.courses.append(course)
        # редирект?
        # return '302 Moved Temporarily', render('create_course.html')
        # Для начала можно без него
        return '200 OK', render('create_course.html')
    else:
        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories)


def create_category_view(request):
    if request['method'] == 'POST':
        # метод пост
        data = request['data']
        # print(data)
        name = data['name']

        name = Application.decode_value(name)
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)

        site.categories.append(new_category)
        # редирект?
        # return '302 Moved Temporarily', render('create_course.html')
        # Для начала можно без него
        return '200 OK', render('create_category.html')
    else:
        categories = site.categories
        return '200 OK', render('create_category.html', categories=categories)


def copy_course(request):
    request_params = request['request_params']
    # print(request_params)
    name = request_params['name']
    old_course = site.get_course(name)
    if old_course:
        new_name = f'copy_{name}'
        new_course = old_course.clone()
        new_course.name = new_name
        site.courses.append(new_course)

    return '200 OK', render('course_list.html', objects_list=site.courses)


def category_list_view(request):
    LOGGER.debug('Список категорий')
    return '200 OK', render('category_list.html', objects_list=site.categories)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"


def contact_view(request):
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        LOGGER.debug(
            f'Нам пришло сообщение! Отправитель - '
            f'{Application.decode_value(email)}, '
            f'тема - {Application.decode_value(title)}, текст - '
            f' {Application.decode_value(text)}.'
        )
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')
