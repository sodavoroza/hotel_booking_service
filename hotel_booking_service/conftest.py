import sys, os
project_path = os.path.join(os.path.dirname(__file__), "src")
sys.path.insert(0, project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'