import pytest

from core.hotels.models import Hotel
from core.hotels.services.hotel_service import create_hotel, delete_hotel


@pytest.mark.django_db
def test_create_hotel() -> None:
    hotel_data = {
        "name": "Test Hotel",
        "address": "Test Address",
        "city": "Test City",
    }
    hotel = create_hotel(hotel_data)
    assert hotel.name == "Test Hotel"
    assert hotel.address == "Test Address"
    assert hotel.city == "Test City"


@pytest.mark.django_db
def test_delete_hotel() -> None:
    hotel = Hotel.objects.create(
        name="Test Hotel", address="Test Address", city="Test City"
    )
    assert hotel.id is not None
    result = delete_hotel(hotel.id)
    assert result is True
    assert Hotel.objects.filter(id=hotel.id).count() == 0

    # Test for non-existing hotel
    result = delete_hotel(999)
    assert result is False
