from typing import Any

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet[Booking]):
    """
    ViewSet для управления бронированиями комнат.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Создаёт новое бронирование и возвращает его ID.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return Response({"booking_id": booking.id}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["delete"], url_path="delete")
    def delete_booking(self, request: Request) -> Response:
        """
        Удаляет бронирование по указанному booking_id.
        """
        booking_id = request.data.get("booking_id")
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"], url_path="list-by-room")
    def list_by_room(self, request: Request) -> Response:
        """
        Возвращает список бронирований для заданной комнаты.
        Требует указания параметра room_id.
        """
        room_id = request.query_params.get("room_id")
        if not room_id:
            return Response(
                {"error": "room_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        bookings = Booking.objects.filter(room_id=room_id).order_by("check_in")
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)
