from core.bookings.models import Booking
from core.hotels.tests.base import APIBaseTest
from core.tests.utils.factories import booking_payload_api


class TestBookingAPI(APIBaseTest):
    def test_create_booking_success(self, room) -> None:
        payload = booking_payload_api(room, strict=True)
        response = self.client.post("/api/bookings/", payload, format="json")
        assert response.status_code == 201
        assert "booking_id" in response.json()

    def test_create_overlapping_booking_fail(self, room) -> None:
        Booking.objects.create(
            room=room,
            guest_name="John Doe",
            check_in="2025-06-01",
            check_out="2025-06-05",
        )
        payload = booking_payload_api(
            room, strict=True, check_in="2025-06-04", check_out="2025-06-08"
        )
        response = self.client.post("/api/bookings/", payload, format="json")
        assert response.status_code == 400
        assert "non_field_errors" in response.json()
