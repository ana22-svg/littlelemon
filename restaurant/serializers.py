from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Booking, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory", "description", "category"]


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Booking
        fields = ["id", "name", "no_of_guests", "booking_date", "comment", "user"]
        read_only_fields = ["id", "user"]

    def validate_no_of_guests(self, value):
        if value < 1:
            raise serializers.ValidationError("At least one guest is required.")
        return value

    def create(self, validated_data):
        return Booking.objects.create(user=self.context["request"].user, **validated_data)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
