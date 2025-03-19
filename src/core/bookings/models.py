from django.db import models
from core.hotels.models import Room


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self) -> str:
        return f"Booking for {self.guest_name} in room {self.room.number} at {self.room.hotel.name}"
