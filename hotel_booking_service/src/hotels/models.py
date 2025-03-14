from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)  # Добавлен blank=True, чтобы не требовать обязательность в форме
    address = models.CharField(max_length=255, default="Unknown")
    city = models.CharField(max_length=255, default="Unknown")
    location = models.CharField(max_length=255, default="Unknown")  

    def __str__(self):
        return self.name



class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255, default="Unknown")


    def __str__(self):
        return f"Room {self.number} of {self.hotel.name}"
