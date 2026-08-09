# taskFlow/tasks/urls.py
# Not used yet, but we can create a urls.py file in the tasks app to define app-specific URL patterns. This is useful for organizing URLs related to the tasks app and keeping the main project urls.py file clean.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]