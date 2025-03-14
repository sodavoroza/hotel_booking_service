import pytest
from hotels.models import Hotel
from hotels.services.hotel_service import create_hotel, delete_hotel
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

@pytest.mark.django_db
def test_create_hotel():
    hotel_data = {
        "name": "Test Hotel",
        "address": "Test Address",
        "city": "Test City",
    }
    hotel_data_2 = {
        "name": "Test Hotel 2",
        "address": "Test Address",
        "city": "Test City",
    }
    hotel = create_hotel(hotel_data)[0]  # Извлекаем объект из кортежа
    print(type(hotel))  # Убедитесь, что это <class 'Hotel'>
    assert hotel.name == "Test Hotel"
    assert hotel.address == "Test Address"
    assert hotel.city == "Test City"
    
    hotel = create_hotel(hotel_data_2)[0]
    assert hotel.name == "Test Hotel 2"
    assert hotel.address == "Test Address"
    assert hotel.city == "Test City"

@pytest.mark.django_db
def test_delete_hotel():
    hotel = Hotel.objects.create(name="Test Hotel", address="Test Address", city="Test City")
    result = delete_hotel(hotel.id)
    assert result is True
    assert Hotel.objects.filter(id=hotel.id).count() == 0

    # Test for non-existing hotel
    result = delete_hotel(999)
    assert result is False
