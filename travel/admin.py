from django.contrib import admin
from .models import Trip  # Importa tu modelo (ajusta el nombre según tu modelo)

class TripAdmin(admin.ModelAdmin):
    list_display = ('destination', 'leaving_date', 'return_date', 'description')


admin.site.register(Trip, TripAdmin)
