# travel/urls.py
from django.urls import path

from django.contrib import admin
from .views import contact, home, trip_details

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el administrador
    path('contact/', contact, name='contact'),
    path('', home, name='home'),
    path('trip-details/', trip_details, name='trip_details'),
]
