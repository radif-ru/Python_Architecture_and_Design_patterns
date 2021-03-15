from my_framework import render


def main_view(request):
    my_key = request.get('my_key', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', my_key=my_key)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"
