from django.db import models


# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    leaving_date = models.DateField()
    return_date = models.DateField()
    itinerary = models.TextField()
    image = models.ImageField(upload_to='trip_images/')

    def __str__(self):
        return self.destination
