from rest_framework import serializers

from .models import Hotel, Room


class RoomSerializer(serializers.ModelSerializer["Room"]):
    class Meta:
        model = Room
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer["Hotel"]):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = "__all__"

    def validate_name(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("Имя отеля не может быть пустым.")
        return value
