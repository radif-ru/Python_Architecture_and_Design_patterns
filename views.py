from my_framework import render


def main_view(request):
    my_key, my_title = request.get(
        'my_key', None), request.get('my_title', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', my_key=my_key, my_title=my_title)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"
