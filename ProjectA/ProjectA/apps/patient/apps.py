from django.apps import AppConfig

class PatientsConfig(AppConfig):
    name = 'patients'

    verbose_name = 'Patients'

    def ready(self):
        from . import signals  
