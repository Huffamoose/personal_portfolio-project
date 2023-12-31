from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)  # This will make our model visible on the admin page
