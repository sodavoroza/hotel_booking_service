from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)  # type: ignore
    address = models.CharField(max_length=255, default="Unknown")  # type: ignore
    city = models.CharField(max_length=255, default="Unknown")  # type: ignore
    location = models.CharField(max_length=255, default="Unknown")  # type: ignore

    def __str__(self) -> str:
        return str(self.name)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")  # type: ignore
    number = models.CharField(max_length=10)  # type: ignore
    capacity = models.PositiveIntegerField()  # type: ignore
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)  # type: ignore
    address = models.CharField(max_length=255, default="Unknown")  # type: ignore

    def __str__(self) -> str:
        return f"Room {self.number} of {self.hotel.name}"
