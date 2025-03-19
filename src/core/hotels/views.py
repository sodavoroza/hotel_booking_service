import json
from typing import Any

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from core.hotels.models import Hotel, Room
from core.hotels.serializers import HotelSerializer, RoomSerializer
from core.hotels.services.hotel_service import create_hotel, delete_hotel


class HotelViewSet(viewsets.ModelViewSet[Hotel]):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomViewSet(viewsets.ModelViewSet[Room]):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering")
        if ordering in ["price_per_night", "-price_per_night", "id", "-id"]:
            queryset = queryset.order_by(ordering)
        return queryset


class RoomDeleteView(APIView):
    def delete(self, request, pk, format=None) -> Response:
        try:
            room = Room.objects.get(id=pk)
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Room.DoesNotExist:
            return Response(
                {"detail": "Room not found."}, status=status.HTTP_404_NOT_FOUND
            )


@method_decorator(csrf_exempt, name="dispatch")
class HotelCreateView(View):
    def post(self, request: Any, *args: Any, **kwargs: Any) -> JsonResponse:
        data = json.loads(request.body)
        try:
            hotel: Hotel = create_hotel(data)
            serializer = HotelSerializer(hotel)
            return JsonResponse(serializer.data, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)


class HotelDetailView(APIView):
    def get(self, request: Any, pk: int, format: Any = None) -> Response:
        try:
            hotel: Hotel = Hotel.objects.get(id=pk)
            serializer = HotelSerializer(hotel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Hotel.DoesNotExist:
            return Response(
                {"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND
            )


class HotelUpdateView(APIView):
    def put(self, request: Any, pk: int, format: Any = None) -> Response:
        try:
            hotel: Hotel = Hotel.objects.get(id=pk)
            serializer = HotelSerializer(hotel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Hotel.DoesNotExist:
            return Response(
                {"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND
            )


class HotelPartialUpdateView(APIView):
    def patch(self, request: Any, pk: int, format: Any = None) -> Response:
        try:
            hotel: Hotel = Hotel.objects.get(id=pk)
            serializer = HotelSerializer(hotel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Hotel.DoesNotExist:
            return Response(
                {"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND
            )


class HotelDeleteView(APIView):
    def delete(self, request: Any, pk: int, format: Any = None) -> Response:
        if delete_hotel(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND
        )
