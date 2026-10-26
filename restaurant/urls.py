from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, LoginView, MenuItemViewSet, RegistrationView

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="booking")
router.register("booking", BookingViewSet, basename="booking-singular")

urlpatterns = [
    path("", include(router.urls)),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
]
