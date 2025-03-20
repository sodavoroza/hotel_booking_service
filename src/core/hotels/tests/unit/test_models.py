import pytest
from core.hotels.models import Hotel, Room
from core.tests.utils.factories import hotel_payload, room_payload_model


@pytest.mark.django_db
def test_hotel_model() -> None:
    hotel: Hotel = Hotel.objects.create(**hotel_payload(strict=True))
    assert hotel.name == "Test Hotel"
    assert hotel.address == "Test Address"
    assert hotel.city == "Test City"
    assert hotel.location == "Test Location"
    assert str(hotel) == "Test Hotel"


@pytest.mark.django_db
def test_room_model() -> None:
    hotel: Hotel = Hotel.objects.create(**hotel_payload(strict=True))
    room: Room = Room.objects.create(**room_payload_model(hotel, strict=True))
    assert room.hotel == hotel
    assert room.number == "101"
    assert room.capacity == 2
    assert room.price_per_night == 100.00
    assert room.address == "Standard Room"
    assert str(room) == f"Room {room.number} of {hotel.name}"
