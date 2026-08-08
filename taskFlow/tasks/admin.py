from django.contrib import admin
from .models import Task
# Register your models here.
admin.site.register(Task) # Name of the model to be registered in the admin interface. This allows the Task model to be managed through the Django admin panel.
