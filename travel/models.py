from django.db import models


# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    dates = models.CharField(max_length=100)
    itinerary = models.TextField()
    image = models.ImageField(upload_to='trip_images/')

    def __str__(self):
        return self.destination
