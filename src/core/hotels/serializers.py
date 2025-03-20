from rest_framework import serializers

from core.hotels.models import Hotel, Room


class RoomSerializer(serializers.ModelSerializer[Room]):
    """
    Сериализатор модели Room, описывает данные комнаты в отеле.
    """

    class Meta:
        model = Room
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer[Hotel]):
    """
    Сериализатор модели Hotel, включая вложенные данные о комнатах.
    """

    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = "__all__"

    def validate_name(self, value: str) -> str:
        """
        Проверяет, что имя отеля не пустое.

        Args:
            value (str): Имя отеля.

        Raises:
            serializers.ValidationError: если имя пустое или состоит из пробелов.

        Returns:
            str: проверенное имя отеля.
        """
        if not value.strip():
            raise serializers.ValidationError("Имя отеля не может быть пустым.")
        return value
