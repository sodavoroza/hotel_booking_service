from core.hotels.models import Room
from core.hotels.tests.base import APIBaseTest
from core.tests.utils.factories import room_payload_api, room_payload_model


class TestRoomAPI(APIBaseTest):
    def test_create_room(self, hotel):
        payload = room_payload_api(hotel, strict=True)
        response = self.client.post("/api/rooms/", payload, format="json")
        assert response.status_code == 201
        assert response.json()["number"] == payload["number"]

    def test_list_rooms(self, hotel):
        Room.objects.create(**room_payload_model(hotel, strict=True))
        Room.objects.create(**room_payload_model(hotel, strict=True, number="102"))
        response = self.client.get("/api/rooms/")
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_sort_rooms_by_price(self, hotel):
        Room.objects.create(
            **room_payload_model(hotel, strict=True, price_per_night=120)
        )
        Room.objects.create(
            **room_payload_model(hotel, strict=True, number="102", price_per_night=180)
        )
        response = self.client.get("/api/rooms/?ordering=price_per_night")
        rooms = response.json()
        assert rooms[0]["price_per_night"] == "120.00"
        assert rooms[1]["price_per_night"] == "180.00"

    def test_delete_room(self, room):
        response = self.client.delete(f"/api/rooms/{room.id}/")
        assert response.status_code == 204
