from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from excel_import.models import FoodModel
from likeapp.serializers import FoodModelSerializer


# Create your views here.

class FoodModelViewSet(viewsets.ModelViewSet):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, food_id):
    food = FoodModel.objects.get(pk=food_id)

    if request.user in food.liked_users.all():
        # 이미 좋아요를 눌렀으면 좋아요 해제
        food.liked_users.remove(request.user)
    else:
        # 좋아요 추가
        food.liked_users.add(request.user)

    return redirect('menu_detail', food_id=food_id)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_like_status(request, food_id):
    food = FoodModel.objects.get(pk=food_id)
    if food.liked_users.filter(pk=request.user.id).exists():
        is_liked = True
    else:
        is_liked = False
    return Response({'is_liked': is_liked})