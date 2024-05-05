from django.apps import AppConfig

class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProjectB.patients'

    def ready(self):
        pass
