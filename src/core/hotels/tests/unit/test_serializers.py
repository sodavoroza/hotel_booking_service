import pytest
from core.hotels.models import Hotel
from core.hotels.serializers import HotelSerializer, RoomSerializer
from core.tests.utils.factories import hotel_payload, room_payload_api


@pytest.mark.django_db
def test_hotel_serializer_create() -> None:
    serializer = HotelSerializer(data=hotel_payload(strict=True))
    assert serializer.is_valid()
    hotel = serializer.save()
    assert hotel.name == "Test Hotel"
    assert hotel.address == "Test Address"
    assert hotel.city == "Test City"


@pytest.mark.django_db
def test_hotel_serializer_invalid() -> None:
    invalid_data = hotel_payload(strict=True, name="")
    serializer = HotelSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert "name" in serializer.errors


@pytest.mark.django_db
def test_hotel_serializer_update() -> None:
    hotel = Hotel.objects.create(**hotel_payload(strict=True))
    updated_data = hotel_payload(strict=True, name="Updated Hotel")
    serializer = HotelSerializer(hotel, data=updated_data)
    assert serializer.is_valid()
    updated_hotel = serializer.save()
    assert updated_hotel.name == "Updated Hotel"


@pytest.mark.django_db
def test_room_serializer_create() -> None:
    hotel = Hotel.objects.create(**hotel_payload(strict=True))
    serializer = RoomSerializer(data=room_payload_api(hotel, strict=True))
    assert serializer.is_valid()
    room = serializer.save()
    assert room.hotel == hotel
    assert room.number == "101"


@pytest.mark.django_db
def test_room_serializer_invalid() -> None:
    hotel = Hotel.objects.create(**hotel_payload(strict=True))
    data = room_payload_api(hotel, strict=True, number="")
    serializer = RoomSerializer(data=data)
    assert not serializer.is_valid()
    assert "number" in serializer.errors
