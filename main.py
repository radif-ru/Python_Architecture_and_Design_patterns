from wsgiref.simple_server import make_server

from logging_mod import Logger
from my_framework import Application, render, DebugApplication, FakeApplication
import views

LOGGER = Logger('main')

urlpatterns = {
    '/': views.main_view,
    # '/about/': views.about_view,
    # '/contact/': views.contact_view,

    '/create-course/': views.create_course_view,
    '/create-category/': views.create_category_view,
    '/course-list/': views.course_list_view,
    '/copy-course/': views.copy_course,
    '/category-list/': views.category_list_view,
}


def my_controller(request):
    # пример Front Controller
    request['my_key'] = 'Hello World!'
    request['my_title'] = 'My framework'


front_controllers = [
    my_controller
]

application = Application(urlpatterns, front_controllers)


# application = DebugApplication(urlpatterns, front_controllers)
# application = FakeApplication(urlpatterns, front_controllers)

@application.add_route('/about/')
def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"


@application.add_route('/contact/')
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


# Утилита для запуска сервера на Windows!
with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
