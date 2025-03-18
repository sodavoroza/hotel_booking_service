from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
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
