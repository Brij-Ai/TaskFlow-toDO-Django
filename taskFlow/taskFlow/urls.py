"""
URL configuration for taskFlow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.template.backends import django
from django.urls import path, include
from django.conf import settings
from tasks import views
from django.conf.urls.static import static

from django.contrib.auth.urls import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # Add a URL pattern for the home view
    # path('', views.home, name='home'),
    path('', include('tasks.urls')), # Include the tasks app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

