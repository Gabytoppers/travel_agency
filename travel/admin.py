from django.contrib import admin
from .models import Trip  # Importa tu modelo (ajusta el nombre según tu modelo)

class TripAdmin(admin.ModelAdmin):
    list_display = ('destination', 'dates', 'description')


admin.site.register(Trip, TripAdmin)
