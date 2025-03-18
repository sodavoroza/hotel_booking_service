import pytest
from bookings.models import Booking
from hotels.models import Hotel, Room


@pytest.fixture
def hotel():
    return Hotel.objects.create(
        name="Test Hotel", address="123 Street", city="Paris", location="Center"
    )


@pytest.fixture
def room(hotel):
    return Room.objects.create(
        hotel=hotel, number="101", capacity=2, price_per_night=120.0, address="Floor 1"
    )


@pytest.fixture
def booking(room):
    return Booking.objects.create(
        room=room, guest_name="John Doe", check_in="2025-06-01", check_out="2025-06-05"
    )
