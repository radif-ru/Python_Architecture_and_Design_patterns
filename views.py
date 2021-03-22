from my_framework import render, Application
# Инициализация логирования сервера.
from logs.configs.config_server_log import LOGGER


def main_view(request):
    my_key, my_title = request.get(
        'my_key', None), request.get('my_title', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', my_key=my_key, my_title=my_title)


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
        print(
            f'Нам пришло сообщение! Отправитель - '
            f'{Application.decode_value(email)}, '
            f'тема - {Application.decode_value(title)}, текст - '
            f' {Application.decode_value(text)}.')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')


def category_list_view(request):
    return '200 OK', render('category_list.html')


def course_list_view(request):
    return '200 OK', render('course_list.html')


def create_category_view(request):
    return '200 OK', render('create_category.html')


def create_course_view(request):
    return '200 OK', render('create_course.html')
