import os
import sys

import django

# Указываем путь к проекту
project_path = os.path.join(os.path.dirname(__file__), "src")
sys.path.insert(0, project_path)

# Устанавливаем переменную окружения для Django
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

# Инициализируем Django
django.setup()
