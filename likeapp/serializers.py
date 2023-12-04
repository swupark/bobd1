# serializers.py
from rest_framework import serializers

from excel_import.models import FoodModel


class FoodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = ('id', 'liked_users',)
