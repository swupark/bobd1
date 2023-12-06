from rest_framework import serializers

class RecommendListSerializer(serializers.Serializer):
    index = serializers.IntegerField(write_only=True)

    recipe_name = serializers.CharField(write_only=True,max_length=255)
    img_url=serializers.CharField(write_only=True,max_length=255)
