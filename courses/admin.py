from django.contrib import admin
from .models import Course, Department

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits')
    search_fields = ('code', 'name')