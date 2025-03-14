from hotels.models import Hotel
from hotels.serializers import HotelSerializer

def create_hotel(data: dict):
    """
    Создает отель и возвращает объект модели.
    :param data: Словарь с данными отеля.
    :return: Объект модели Hotel.
    """
    serializer = HotelSerializer(data=data)
    if serializer.is_valid():
        hotel = serializer.save()  # Сохраняем объект модели
        return hotel, 201  # Возвращаем сам объект и статус
    return serializer.errors, 400  # В случае ошибки возвращаем ошибки


def delete_hotel(hotel_id: int) -> bool:
    """
    Функция для удаления отеля по ID.
    :param hotel_id: ID отеля, который нужно удалить.
    :return: True, если удаление прошло успешно, иначе False.
    """
    try:
        hotel = Hotel.objects.get(id=hotel_id)
        hotel.delete()
        return True
    except Hotel.DoesNotExist:
        return False
