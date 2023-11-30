from rest_framework import serializers

class RecommendListSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    recipe_name = serializers.CharField(max_length=255)
    similarity = serializers.FloatField()
    new_train = serializers.CharField(max_length=255)
    recipe_way2 = serializers.CharField(max_length=10)
