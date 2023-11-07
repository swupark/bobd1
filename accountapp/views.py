from random import shuffle

from django.shortcuts import render, get_object_or_404
from excel_import.models import FoodModel
def homepage(request):
    vegan_img = list(FoodModel.objects.filter(VEGAN=1).all())
    hp_img = list(FoodModel.objects.filter(HIGH_PRO=1).all())
    ln_img = list(FoodModel.objects.filter(LOW_NA=1).all())
    dt_img = list(FoodModel.objects.filter(DIETS=1).all())
    # vegan = list(FoodModel.objects.values('VEGAN'))
    # vegan = list(FoodModel.objects.values('VEGAN'))
    # vegan = list(FoodModel.objects.values('VEGAN'))
    # vegan = list(FoodModel.objects.values('VEGAN'))
    shuffle(vegan_img)
    shuffle(hp_img)
    shuffle(ln_img)
    shuffle(dt_img)
    return render(request, 'accountapp/home.html',{'vegan_img': vegan_img, 'hp_img': hp_img, 'ln_img': ln_img, 'dt_img': dt_img})


def details(request,imageId):
    rcp = get_object_or_404(FoodModel, id=imageId)
    return render(request,'accountapp/details.html',{'post':imageId, 'rcp':rcp})
