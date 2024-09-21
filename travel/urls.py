# travel/urls.py
from django.urls import path
from django.contrib import admin
from .views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
]