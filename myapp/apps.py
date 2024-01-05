import sys

from django.apps import AppConfig
from django.core.management import call_command

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    def ready(self):
        if 'runserver' in sys.argv:
            from django.core.management import  call_command
            call_command('train_model')