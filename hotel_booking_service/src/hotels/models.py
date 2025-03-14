from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
