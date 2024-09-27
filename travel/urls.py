# travel/urls.py
from django.urls import path

from .views import contact, home, trip_details

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('', home, name='home'),
    path('trip-details/', trip_details, name='trip_details'),
]
