from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from excel_import.models import FoodModel


# Create your views here.

@api_view(['POST'])
def toggle_like(request, food_id):
    food = FoodModel.objects.get(pk=food_id)

    if request.user in food.liked_users.all():
        # 이미 좋아요를 눌렀으면 좋아요 해제
        food.liked_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가
        food.liked_users.add(request.user)
        is_liked = True

    return JsonResponse({'is_liked': is_liked})

@api_view(['GET'])
def check_like_status(request, food_id):
    food = FoodModel.objects.get(pk=food_id)
    if food.liked_users.filter(pk=request.user.id).exists():
        is_liked = True
    else:
        is_liked = False
    return Response({'is_liked': is_liked})

@api_view(['POST'])
def delete_like(request, food_id):
    food = FoodModel.objects.get(pk=food_id)
    food.liked_users.remove(request.user)
    return redirect('mypageapp:mypage', pk=request.user.id)


