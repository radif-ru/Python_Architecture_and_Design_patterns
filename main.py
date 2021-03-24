from my_framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
    '/contact/': views.contact_view,

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
