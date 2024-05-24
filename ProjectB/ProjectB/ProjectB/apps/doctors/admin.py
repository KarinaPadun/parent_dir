from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'email', 'phone_number')
    search_fields = ('name', 'specialization', 'email', 'phone_number')
