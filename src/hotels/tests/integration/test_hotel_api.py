from hotels.tests.base import APIBaseTest
from tests.utils.factories import hotel_payload


class TestHotelAPI(APIBaseTest):
    def test_create_hotel(self):
        payload = hotel_payload(strict=True)
        response = self.client.post("/api/hotels/", payload, format="json")
        assert response.status_code == 201
        assert response.json()["name"] == payload["name"]
