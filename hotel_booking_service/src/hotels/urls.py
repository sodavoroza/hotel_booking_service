from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet

router = DefaultRouter()
router.register(r"", HotelViewSet, basename="hotels")
router.register(r"rooms", RoomViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
