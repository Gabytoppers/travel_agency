# travel/urls.py
from django.urls import path
from .views import hello_world, contact

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('contact/', contact, name='contact'),
]