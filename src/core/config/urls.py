from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.hotels.views import HotelViewSet, RoomViewSet
from core.bookings.views import BookingViewSet
from django.conf import settings

router = DefaultRouter()
router.register(r"hotels", HotelViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", lambda request: HttpResponse("Главная страница заглушка 👋")),
]

if settings.DEBUG:
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    from rest_framework import permissions

    schema_view = get_schema_view(
        openapi.Info(
            title="Hotel Booking API",
            default_version="v1",
            description="Это API для бронирования отелей: отели, комнаты и бронирования. 📚",
            terms_of_service="https://example.com/terms/",
            contact=openapi.Contact(email="support@hotelbooking.com"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
