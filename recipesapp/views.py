from django.shortcuts import render
from .models import FoodModel

def menu_detail(request, food_id):
    menu = FoodModel.objects.get(pk=food_id)

    return render(request, 'menu_detail.html', {'menu': menu, 'food_id': food_id})