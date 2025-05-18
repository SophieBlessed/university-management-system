from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'department')
    search_fields = ('staff_id', 'first_name', 'last_name')
    list_filter = ('department',)
