
from django.apps import AppConfig

class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
    verbose_name = 'Student Management'  # This will show up as the name of the app in Django Admin
