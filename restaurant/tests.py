from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

from .models import MenuItem


class RestaurantApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="strong-password")
        self.client.force_authenticate(self.user)

    def test_menu_list_is_public(self):
        MenuItem.objects.create(title="Pasta", price="12.50", inventory=5)
        self.client.force_authenticate(None)
        response = self.client.get(reverse("menu-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Pasta")

    def test_menu_mutations_require_authentication(self):
        self.client.force_authenticate(None)
        response = self.client.post(reverse("menu-list"), {"title": "Salad", "price": "8.00", "inventory": 3})
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_booking(self):
        response = self.client.post(
            reverse("booking-list"),
            {"name": "Alex", "no_of_guests": 2, "booking_date": (timezone.now() + timedelta(days=1)).isoformat()},
        )
        self.assertEqual(response.status_code, 201)
