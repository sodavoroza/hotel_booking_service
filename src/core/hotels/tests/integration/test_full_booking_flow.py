from typing import Any, Dict

import pytest
from core.tests.utils.factories import (
    booking_payload_api,
    hotel_payload,
    room_payload_api,
)
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_full_booking_flow() -> None:
    client = APIClient()

    hotel_resp = client.post("/api/hotels/", hotel_payload(strict=True), format="json")
    hotel: Dict[str, Any] = hotel_resp.json()
    room_resp = client.post(
        "/api/rooms/", room_payload_api(hotel, strict=True), format="json"
    )
    room: Dict[str, Any] = room_resp.json()

    booking_resp = client.post(
        "/api/bookings/", booking_payload_api(room, strict=True), format="json"
    )
    assert booking_resp.status_code == status.HTTP_201_CREATED
    booking_id = booking_resp.json()["booking_id"]

    booking_list_resp = client.get(f"/api/bookings/list-by-room/?room_id={room['id']}")
    assert booking_list_resp.status_code == status.HTTP_200_OK
    bookings = booking_list_resp.json()
    assert any(b["id"] == booking_id for b in bookings)


@pytest.mark.django_db
def test_booking_conflict() -> None:
    client = APIClient()

    hotel: Dict[str, Any] = client.post(
        "/api/hotels/", hotel_payload(strict=True), format="json"
    ).json()
    room: Dict[str, Any] = client.post(
        "/api/rooms/", room_payload_api(hotel, strict=True), format="json"
    ).json()

    booking1 = client.post(
        "/api/bookings/",
        booking_payload_api(
            room, strict=True, check_in="2025-07-01", check_out="2025-07-05"
        ),
    )
    assert booking1.status_code == status.HTTP_201_CREATED

    booking2 = client.post(
        "/api/bookings/",
        booking_payload_api(
            room, strict=True, check_in="2025-07-04", check_out="2025-07-10"
        ),
    )
    assert booking2.status_code == status.HTTP_400_BAD_REQUEST
    assert "non_field_errors" in booking2.json()


@pytest.mark.django_db
def test_cascade_delete_hotel_and_rooms() -> None:
    client = APIClient()

    hotel: Dict[str, Any] = client.post(
        "/api/hotels/", hotel_payload(strict=True), format="json"
    ).json()
    client.post("/api/rooms/", room_payload_api(hotel, strict=True), format="json")
    client.post(
        "/api/rooms/", room_payload_api(hotel, strict=True, number="202"), format="json"
    )

    response = client.delete(f"/api/hotels/{hotel['id']}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    room_list = client.get("/api/rooms/")
    assert room_list.status_code == status.HTTP_200_OK
    assert len(room_list.json()) == 0


@pytest.mark.django_db
def test_booking_nonexistent_room() -> None:
    client = APIClient()
    response = client.post(
        "/api/bookings/", booking_payload_api({"id": 9999}, strict=True), format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "room" in response.json()
