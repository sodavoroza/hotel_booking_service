import pytest

from hotels.models import Hotel
from hotels.services.hotel_service import (
    create_hotel,
    delete_hotel,
    get_hotel,
    update_hotel,
)
from tests.utils.factories import hotel_payload


@pytest.mark.django_db
def test_create_hotel_invalid_data() -> None:
    invalid_data = hotel_payload(strict=True, name="")
    with pytest.raises(ValueError):
        create_hotel(invalid_data)


@pytest.mark.django_db
def test_delete_hotel_success() -> None:
    hotel = Hotel.objects.create(**hotel_payload(strict=True))
    assert delete_hotel(hotel.id)
    assert Hotel.objects.filter(id=hotel.id).count() == 0


@pytest.mark.django_db
def test_delete_hotel_not_found() -> None:
    assert not delete_hotel(9999)


@pytest.mark.django_db
def test_get_hotel_found() -> None:
    hotel = Hotel.objects.create(**hotel_payload(strict=True))
    found = get_hotel(hotel.id)
    assert found == hotel


@pytest.mark.django_db
def test_get_hotel_not_found() -> None:
    assert get_hotel(9999) is None


@pytest.mark.django_db
def test_update_hotel_success() -> None:
    hotel = Hotel.objects.create(**hotel_payload(strict=True))
    updated_data = hotel_payload(strict=True, name="Updated Hotel")
    updated = update_hotel(hotel.id, updated_data)
    assert updated.name == "Updated Hotel"


@pytest.mark.django_db
def test_update_hotel_not_found() -> None:
    data = hotel_payload(strict=True, name="Updated Hotel")
    with pytest.raises(ValueError):
        update_hotel(9999, data)


@pytest.mark.django_db
def test_update_hotel_invalid_data() -> None:
    hotel = Hotel.objects.create(**hotel_payload(strict=True))
    invalid_data = hotel_payload(strict=True, name="")
    with pytest.raises(ValueError):
        update_hotel(hotel.id, invalid_data)
