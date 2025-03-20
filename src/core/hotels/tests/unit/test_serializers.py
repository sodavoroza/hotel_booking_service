import pytest
from core.hotels.models import Hotel, Room
from core.hotels.serializers import HotelSerializer, RoomSerializer
from core.tests.utils.factories import hotel_payload, room_payload_api
from rest_framework.serializers import Serializer


@pytest.mark.django_db
def test_hotel_serializer_create() -> None:
    serializer: Serializer[Hotel] = HotelSerializer(data=hotel_payload(strict=True))
    assert serializer.is_valid()
    hotel: Hotel = serializer.save()
    assert hotel.name == "Test Hotel"
    assert hotel.address == "Test Address"
    assert hotel.city == "Test City"


@pytest.mark.django_db
def test_hotel_serializer_invalid() -> None:
    invalid_data = hotel_payload(strict=True, name="")
    serializer: Serializer[Hotel] = HotelSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert "name" in serializer.errors


@pytest.mark.django_db
def test_hotel_serializer_update() -> None:
    hotel: Hotel = Hotel.objects.create(**hotel_payload(strict=True))
    updated_data = hotel_payload(strict=True, name="Updated Hotel")
    serializer: Serializer[Hotel] = HotelSerializer(hotel, data=updated_data)
    assert serializer.is_valid()
    updated_hotel: Hotel = serializer.save()
    assert updated_hotel.name == "Updated Hotel"


@pytest.mark.django_db
def test_room_serializer_create() -> None:
    hotel: Hotel = Hotel.objects.create(**hotel_payload(strict=True))
    serializer: Serializer[Room] = RoomSerializer(
        data=room_payload_api(hotel, strict=True)
    )
    assert serializer.is_valid()
    room: Room = serializer.save()
    assert room.hotel == hotel
    assert room.number == "101"


@pytest.mark.django_db
def test_room_serializer_invalid() -> None:
    hotel: Hotel = Hotel.objects.create(**hotel_payload(strict=True))
    data = room_payload_api(hotel, strict=True, number="")
    serializer: Serializer[Room] = RoomSerializer(data=data)
    assert not serializer.is_valid()
    assert "number" in serializer.errors
