"""Константы"""
import os
from logging import DEBUG, ERROR

PROJECT_PATH = os.getcwd()

LOGS_PATH = os.path.join(PROJECT_PATH, "logs")
LOG_CONFIGS_PATH = os.path.join(LOGS_PATH, "configs")
LOG_FILES_PATH = os.path.join(LOGS_PATH, "log_files")
SERVER_LOG_FILE = os.path.join(LOG_FILES_PATH, "server.log")

ENCODING = 'utf-8'
# Текущий уровень логирования
LOGGING_LEVEL = DEBUG
# Текущий уровень логирования для потокового вывода
LOGGING_LEVEL_FOR_STREAM_HANDLER = ERROR
# на время отладки потоковый вывод иногда так же ставлю в DEBUG
# LOGGING_LEVEL_FOR_STREAM_HANDLER = DEBUG
