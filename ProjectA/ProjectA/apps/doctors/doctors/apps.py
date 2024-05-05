from django.apps import AppConfig

class DoctorsConfig(AppConfig):
    name = 'doctors'

    verbose_name = 'Doctors'

    def ready(self):
        from . import signals  
