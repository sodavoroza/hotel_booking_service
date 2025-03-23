from typing import Any, Dict

from core.hotels.models import Hotel
from core.hotels.serializers import HotelSerializer


def create_hotel(data: Dict[str, Any]) -> Hotel:
    """
    Создает и сохраняет новый объект отеля.

    :param data: Данные отеля
    :return: Сохранённый объект отеля
    :raises ValueError: если данные некорректны
    """
    serializer = HotelSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    raise ValueError(f"Invalid hotel data provided: {serializer.errors}")


def delete_hotel(hotel_id: int) -> bool:
    """
    Удаляет отель по его ID.

    :param hotel_id: Идентификатор отеля.
    :return: True, если отель был удален, False если не найден.
    """
    hotel = Hotel.objects.filter(id=hotel_id).first()
    if hotel:
        hotel.delete()
        return True
    return False


def get_hotel(hotel_id: int) -> Hotel | None:
    """
    Возвращает отель по его ID.

    :param hotel_id: Идентификатор отеля.
    :return: Отель или None, если отель не найден.
    """
    return Hotel.objects.filter(id=hotel_id).first()


def update_hotel(hotel_id: int, data: Dict[str, Any]) -> Hotel:
    """
    Обновляет данные существующего отеля.

    :param hotel_id: Идентификатор отеля.
    :param data: Данные для обновления.
    :return: Обновлённый объект Hotel.
    """
    hotel = Hotel.objects.filter(id=hotel_id).first()
    if hotel:
        serializer = HotelSerializer(hotel, data=data, partial=True)
        if serializer.is_valid():
            return serializer.save()
        raise ValueError(f"Invalid data provided: {serializer.errors}")
    raise ValueError(f"Hotel with id {hotel_id} does not exist.")
