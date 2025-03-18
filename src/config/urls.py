from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bookings.views import BookingViewSet
from hotels.views import HotelViewSet, RoomViewSet

router = DefaultRouter()
router.register(r"hotels", HotelViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # теперь это корневой API!
]
