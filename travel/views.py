# travel/views.py
from django.shortcuts import render
from .models import LandingContent


def landing_page(request):
    content = LandingContent.objects.all()
    content = content.first()
    return render(request, 'landing/landing_page.html', {'landing_content': content})
