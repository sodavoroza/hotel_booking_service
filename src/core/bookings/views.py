from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return Response({"booking_id": booking.id}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["delete"], url_path="delete")
    def delete_booking(self, request):
        booking_id = request.data.get("booking_id")
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return Response(
            {"detail": "Booking deleted"}, status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=False, methods=["get"], url_path="list")
    def list_bookings(self, request):
        room_id = request.query_params.get("room_id")
        if not room_id:
            return Response(
                {"error": "room_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        bookings = Booking.objects.filter(room_id=room_id).order_by("check_in")
        data = [
            {"booking_id": b.id, "date_start": b.check_in, "date_end": b.check_out}
            for b in bookings
        ]
        return Response(data, status=status.HTTP_200_OK)
