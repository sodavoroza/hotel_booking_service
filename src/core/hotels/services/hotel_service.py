from typing import Any, Dict, Union

from core.hotels.models import Hotel
from core.hotels.serializers import HotelSerializer


def create_hotel(data: Dict[str, Any]) -> Hotel:
    """
    Создает отель и возвращает объект модели.
    :param data: Словарь с данными отеля.
    :return: Объект модели Hotel.
    """
    serializer = HotelSerializer(data=data)
    if serializer.is_valid():
        hotel: Hotel = serializer.save()  # Сохраняем объект модели
        return hotel  # Возвращаем только объект модели
    raise ValueError("Invalid data for creating hotel: " + str(serializer.errors))


def delete_hotel(hotel_id: int) -> bool:
    """
    Функция для удаления отеля по ID.
    :param hotel_id: ID отеля, который нужно удалить.
    :return: True, если удаление прошло успешно, иначе False.
    """
    try:
        hotel: Hotel = Hotel.objects.get(id=hotel_id)
        hotel.delete()
        return True
    except Hotel.DoesNotExist:
        return False


def get_hotel(hotel_id: int) -> Union[Hotel, None]:
    """
    Получает отель по ID.
    :param hotel_id: ID отеля.
    :return: Объект модели Hotel или None.
    """
    try:
        return Hotel.objects.get(id=hotel_id)
    except Hotel.DoesNotExist:
        return None


def update_hotel(hotel_id: int, data: Dict[str, Any]) -> Hotel:
    """
    Обновляет данные отеля.
    :param hotel_id: ID отеля, который нужно обновить.
    :param data: Данные для обновления.
    :return: Обновленный объект модели Hotel.
    """
    hotel = get_hotel(hotel_id)
    if hotel:
        serializer = HotelSerializer(hotel, data=data)
        if serializer.is_valid():
            return serializer.save()
        raise ValueError("Invalid data for updating hotel: " + str(serializer.errors))
    raise ValueError(f"Hotel with ID {hotel_id} not found.")
