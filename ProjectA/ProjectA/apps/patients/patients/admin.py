from django.contrib import admin
from .models import Patient, Appointment

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'description')
    list_filter = ('doctor', 'date')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
