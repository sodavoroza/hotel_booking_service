import pytest
from rest_framework.response import Response
from rest_framework.test import APIClient

from core.tests.utils.factories import (
    booking_payload_api,
    hotel_payload,
    room_payload_api,
)


@pytest.mark.django_db
def test_full_booking_flow() -> None:
    client: APIClient = APIClient()

    hotel_resp: Response = client.post("/api/hotels/", hotel_payload(strict=True), format="json")
    hotel = hotel_resp.json()
    room_resp: Response = client.post(
        "/api/rooms/", room_payload_api(hotel, strict=True), format="json"
    )
    room = room_resp.json()

    booking_resp: Response = client.post(
        "/api/bookings/", booking_payload_api(room, strict=True), format="json"
    )
    assert booking_resp.status_code == 201
    booking_id = booking_resp.json()["booking_id"]

    booking_list_resp: Response = client.get(f"/api/bookings/list/?room_id={room['id']}")
    assert booking_list_resp.status_code == 200
    bookings = booking_list_resp.json()
    assert any(b["booking_id"] == booking_id for b in bookings)


@pytest.mark.django_db
def test_booking_conflict() -> None:
    client: APIClient = APIClient()

    hotel = client.post(
        "/api/hotels/", hotel_payload(strict=True), format="json"
    ).json()
    room = client.post(
        "/api/rooms/", room_payload_api(hotel, strict=True), format="json"
    ).json()

    booking1: Response = client.post(
        "/api/bookings/",
        booking_payload_api(
            room, strict=True, check_in="2025-07-01", check_out="2025-07-05"
        ),
    )
    assert booking1.status_code == 201

    booking2: Response = client.post(
        "/api/bookings/",
        booking_payload_api(
            room, strict=True, check_in="2025-07-04", check_out="2025-07-10"
        ),
    )
    assert booking2.status_code == 400
    assert "non_field_errors" in booking2.json()


@pytest.mark.django_db
def test_cascade_delete_hotel_and_rooms() -> None:
    client: APIClient = APIClient()

    hotel = client.post(
        "/api/hotels/", hotel_payload(strict=True), format="json"
    ).json()
    client.post("/api/rooms/", room_payload_api(hotel, strict=True), format="json")
    client.post(
        "/api/rooms/", room_payload_api(hotel, strict=True, number="202"), format="json"
    )

    response: Response = client.delete(f"/api/hotels/{hotel['id']}/")
    assert response.status_code == 204

    room_list: Response = client.get("/api/rooms/")
    assert room_list.status_code == 200
    assert len(room_list.json()) == 0


@pytest.mark.django_db
def test_booking_nonexistent_room() -> None:
    client: APIClient = APIClient()
    response: Response = client.post(
        "/api/bookings/", booking_payload_api({"id": 9999}, strict=True), format="json"
    )
    assert response.status_code == 400
    assert "room" in response.json()
