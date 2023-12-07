# serializers.py
from rest_framework import serializers
from excel_import.models import FoodModel

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = ('id', 'ATT_FILE_NO_MAIN','RCP_NM','LOW_NA','HIGH_PRO','VEGAN','DIETS',)

class UserLikedRecipesSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    liked_recipes = FoodSerializer(many=True)
