import json
from typing import Any

from django.http import HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.hotels.models import Hotel, Room
from core.hotels.serializers import HotelSerializer, RoomSerializer
from core.hotels.services.hotel_service import create_hotel, delete_hotel


class HotelViewSet(viewsets.ModelViewSet[Hotel]):
    """
    ViewSet для управления отелями с использованием стандартных CRUD-операций DRF.
    """

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomViewSet(viewsets.ModelViewSet[Room]):
    """
    ViewSet для управления комнатами отелей с поддержкой сортировки.
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self) -> Any:
        """
        Возвращает список комнат с возможностью сортировки по указанным параметрам.

        Доступные параметры сортировки:
            - price_per_night (цена за ночь)
            - id (идентификатор комнаты)

        Параметр сортировки задается в query_params['ordering'].

        Returns:
            QuerySet: отсортированный набор комнат.
        """
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering")
        if ordering in ["price_per_night", "-price_per_night", "id", "-id"]:
            queryset = queryset.order_by(ordering)
        return queryset


class RoomDeleteView(APIView):
    """
    API endpoint для удаления комнаты по её идентификатору.
    """

    def delete(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Удаляет указанную комнату.

        Args:
            request (Request): HTTP-запрос.
            pk (int): ID комнаты.

        Returns:
            Response: HTTP-ответ с результатом операции.
        """
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
    """
    API endpoint для создания отеля через стандартный Django View.
    """

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
        """
        Создает новый отель.

        Args:
            request (HttpRequest): HTTP-запрос с данными отеля.

        Returns:
            JsonResponse: Ответ с информацией о созданном отеле или об ошибке.
        """
        data = json.loads(request.body)
        try:
            hotel: Hotel = create_hotel(data)
            serializer = HotelSerializer(hotel)
            return JsonResponse(serializer.data, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)


class HotelDetailView(APIView):
    """
    API endpoint для получения детальной информации об отеле по ID.
    """

    def get(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Возвращает информацию об отеле.

        Args:
            request (Request): HTTP-запрос.
            pk (int): ID отеля.

        Returns:
            Response: Ответ с данными об отеле или ошибка, если отель не найден.
        """
        try:
            hotel: Hotel = Hotel.objects.get(id=pk)
            serializer = HotelSerializer(hotel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Hotel.DoesNotExist:
            return Response(
                {"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND
            )


class HotelUpdateView(APIView):
    """
    API endpoint для полного обновления информации об отеле.
    """

    def put(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Обновляет отель целиком.

        Args:
            request (Request): HTTP-запрос.
            pk (int): ID отеля.

        Returns:
            Response: Ответ с обновленными данными отеля или описание ошибок.
        """
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
    """
    API endpoint для частичного обновления информации об отеле.
    """

    def patch(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Частично обновляет данные отеля.

        Args:
            request (Request): HTTP-запрос.
            pk (int): ID отеля.

        Returns:
            Response: Ответ с частично обновленными данными отеля или описание ошибок.
        """
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
    """
    API endpoint для удаления отеля по его идентификатору.
    """

    def delete(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Удаляет отель по идентификатору.

        Args:
            request (Request): HTTP-запрос.
            pk (int): ID отеля.

        Returns:
            Response: HTTP-ответ с результатом операции удаления.
        """
        if delete_hotel(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND
        )
