from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer
from .services.hotel_service import create_hotel, delete_hotel

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def destroy(self, request, *args, **kwargs):
        hotel_id = kwargs.get('pk')
        if delete_hotel(hotel_id):  # Вызываем сервис для удаления
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# Дополнительный endpoint для создания отеля через сервисный слой
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.views import View

class HotelCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)  # Парсим входящие данные
        try:
            hotel = create_hotel(data)  # Создаем отель через сервис
            serializer = HotelSerializer(hotel)
            return JsonResponse(serializer.data, status=201)  # Возвращаем данные нового отеля
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

class HotelDeleteView(APIView):
    def delete(self, request, pk, format=None):
        if delete_hotel(pk):  # Вызываем сервис для удаления
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND)
