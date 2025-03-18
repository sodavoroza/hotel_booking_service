from bookings.views import BookingViewSet
from django.contrib import admin
from django.urls import include, path
from hotels.views import HotelViewSet, RoomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"hotels", HotelViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # теперь это корневой API!
]
