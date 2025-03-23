from django.db import models


class Hotel(models.Model):
    """
    Модель, представляющая отель.

    Атрибуты:
        name (str): Название отеля.
        address (str): Адрес отеля.
        city (str): Город, в котором расположен отель.
        location (str): Конкретное местоположение отеля (район и т.п.).
    """

    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, default="Unknown")
    city = models.CharField(max_length=255, default="Unknown")
    location = models.CharField(max_length=255, default="Unknown")

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    """
    Комната (номер) в отеле.

    Attributes:
        hotel: Отель, к которому относится комната.
        number: Номер комнаты.
        capacity: Вместимость комнаты (количество гостей).
        price_per_night: Цена за одну ночь проживания.
        address: Дополнительная информация о комнате (например, этаж).
    """

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255, default="Unknown")

    def __str__(self) -> str:
        return f"Room {self.number} of {self.hotel.name}"
