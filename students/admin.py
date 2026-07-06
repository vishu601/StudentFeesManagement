from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'roll_no',
        'name',
        'student_class',
        'section',
        'mobile',
    )

    search_fields = (
        'name',
        'roll_no',
        'mobile',
    )

    list_filter = (
        'student_class',
        'section',
        'gender',
    )