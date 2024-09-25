# travel/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Trip


def contact(request):
    return render(request, 'contact.html')


def home(request):
    trips = Trip.objects.all()
    return render(request, 'home.html', {'trips': trips})


def trip_details(request):
    trip_id = request.POST.get('trip')
    trip = Trip.objects.get(id=trip_id)
    print(trip)
    return render(request, 'trip_details.html', {'trip': trip})
