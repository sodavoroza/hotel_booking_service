from typing import Any

from rest_framework import serializers

from core.bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer[Booking]):
    """
    Сериализатор модели Booking, включающий валидацию дат и проверку на пересечения бронирований.
    """

    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Проверяет, что даты бронирования корректны и комната свободна на указанный период.

        Args:
            data (dict): Данные для бронирования.

        Raises:
            serializers.ValidationError: Если дата начала позже или равна дате окончания,
                                         или если комната уже забронирована на выбранные даты.

        Returns:
            dict: Валидированные данные.
        """
        check_in = data.get("check_in")
        check_out = data.get("check_out")
        room = data.get("room")

        if check_in and check_out and check_in >= check_out:
            raise serializers.ValidationError(
                "Дата начала брони должна быть раньше даты окончания."
            )

        overlapping = Booking.objects.filter(
            room=room, check_out__gt=check_in, check_in__lt=check_out
        )
        if overlapping.exists():
            raise serializers.ValidationError("Номер уже занят на выбранные даты.")

        return data
