from django.contrib import admin
from .patients.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

admin.site.register(Patient, PatientAdmin)
