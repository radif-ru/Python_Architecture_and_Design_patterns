import time

from reusepatterns.singletones import SingletonByName
# Инициализация логирования сервера.
from logs.configs.config_server_log import LOGGER


# Заметка, можно применить стратегию если добавить стратегию логирования
class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def debug(self, text):
        return LOGGER.debug(text)


# декоратор
def debug(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('DEBUG-------->', func.__name__, end - start)
        return result

    return inner
