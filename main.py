from my_framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
    '/contact/': views.contact_view
}


def my_controller(request):
    # пример Front Controller
    request['my_key'] = 'Hello World!'
    request['my_title'] = 'My framework'


front_controllers = [
    my_controller
]

application = Application(urlpatterns, front_controllers)
