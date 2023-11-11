from django.shortcuts import render
from .models import FoodModel

def menu_detail(request, FOOD_ID):
    menu = FoodModel.objects.get(pk=FOOD_ID)

    return render(request, 'menu_detail.html', {'menu': menu})