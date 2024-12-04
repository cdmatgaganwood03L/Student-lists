
# Register your models here.
from django.contrib import admin
from .models import Student

# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender','ph_num','email', 'age')  # Display these fields in the admin list view
    search_fields = ('first_name', 'last_name', 'email')  # Search functionality in the admin panel
    list_filter = ('age',)  # Add a filter by age in the admin panel
