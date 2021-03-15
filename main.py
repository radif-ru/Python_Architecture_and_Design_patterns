from my_framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
}


def my_controller(request):
    # пример Front Controller
    request['my_key'] = 'Hello World!'


front_controllers = [
    my_controller
]

application = Application(urlpatterns, front_controllers)
