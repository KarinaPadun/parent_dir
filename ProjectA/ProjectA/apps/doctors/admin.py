from django.contrib import admin
from .models import Doctor, Appointment

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'email', 'phone_number')
    search_fields = ('name', 'email', 'phone_number')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'description')
    list_filter = ('doctor', 'date')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
