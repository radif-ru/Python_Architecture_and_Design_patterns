# Python_Architecture_and_Design_patterns
Архитектура и шаблоны проектирования на Python • 08.02.2021 MSK (UTC+3)

# My Framework

Если нет Python:
sudo add-apt-repository universe
sudo apt update
sudo apt install python3-pip

Перед запуском проекта (в Linux/Ubuntu) установить uwsgi или gunicorn:
pip3 install uwsgi

Устанавливаем шаблонизатор Jinja2:
pip3 install jinja2

Для себя, на время работы на виртуальной машине:
Переход в папку проекта:
sudo -i (под рутом в режиме суперпользователя, так как иначе невозможно попасть в общую папку с Windows через терминал, а sudo cd /.../ не работает)
root@radif-VirtualBox:~# cd "/mnt/D_DRIVE/YandexDisk/GeekBrains/Факультет Python-разработки/2.7 Архитектура и шаблоны проектирования на Python/Python_Architecture_and_Design_patterns"
su radif (переходим к обычному пользователю, т.е. выходим из режима суперпользователя и работаем в папке проекта)

Запуск проекта (для нормальной работы в общей с Windows папке всё же приходится использовать права суперпользователя sudo): 
radif@radif-VirtualBox:/mnt/D_DRIVE/YandexDisk/GeekBrains/Факультет Python-разра ботки/2.7 Архитектура и шаблоны проектирования на Python/Python_Architecture_and_Design_patterns$ 
sudo uwsgi --http :8000 --wsgi-file main.py

