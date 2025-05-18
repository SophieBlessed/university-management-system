from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'registration_number')
    list_filter = ('enrolled_courses',)
