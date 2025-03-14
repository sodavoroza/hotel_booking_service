from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, HotelCreateView, HotelDeleteView

router = DefaultRouter()
router.register(r"hotels", HotelViewSet)
router.register(r"rooms", RoomViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # Дополнительные endpoints:
    path("create/", HotelCreateView.as_view(), name="hotel-create"),
    path("<int:pk>/delete/", HotelDeleteView.as_view(), name="hotel-delete"),
]
