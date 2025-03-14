from django.db import models
from hotels.models import Hotel


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
