from django.db import models
#A simple model for a task in the task management application. Each task has a title, description, and a completion status.
from django.contrib.auth.models import User

# Create your models here.
# basic Task model with title, description, completed status, and assigned user. The __str__ method returns the title of the task for easy identification in the admin interface.
# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

class Task(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    completed = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title