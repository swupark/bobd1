from random import shuffle

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator

from accountapp.decorator import account_ownership_required
from excel_import.models import FoodModel

has_ownership=[account_ownership_required, login_required]
def homepage(request):
    dislike_ingredient = request.GET.get('dislike_ingredient', '')
    vegan_img,hp_img,ln_img,dt_img=dislike(dislike_ingredient)
    # if dislike_ingredient:
    #     vegan_img = [recipe for recipe in vegan_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     hp_img = [recipe for recipe in hp_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     ln_img = [recipe for recipe in ln_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     dt_img = [recipe for recipe in dt_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    # shuffle(vegan_img)
    # shuffle(hp_img)
    # shuffle(ln_img)
    # shuffle(dt_img)

    return render(request, 'accountapp/home.html',{'vegan_img': vegan_img, 'hp_img': hp_img, 'ln_img': ln_img, 'dt_img': dt_img})

def details(request,imageId):
    rcp = get_object_or_404(FoodModel, id=imageId)
    return render(request,'accountapp/details.html',{'post':imageId, 'rcp':rcp})

def dislike(dislike_igt):
    # 싫어하는 재료를 입력받습니다.
    dislike_ingredient = dislike_igt

    # 모든 레시피를 가져옵니다.
    vegan_img = list(FoodModel.objects.filter(VEGAN=1).all())
    hp_img = list(FoodModel.objects.filter(HIGH_PRO=1).all())
    ln_img = list(FoodModel.objects.filter(LOW_NA=1).all())
    dt_img = list(FoodModel.objects.filter(DIETS=1).all())

    # 사용자가 입력한 싫어하는 재료가 있을 경우 해당하는 레시피를 제거합니다.
    if dislike_ingredient:
        vegan_img = [recipe for recipe in vegan_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
        hp_img = [recipe for recipe in hp_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
        ln_img = [recipe for recipe in ln_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
        dt_img = [recipe for recipe in dt_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    else:
        return (vegan_img, hp_img, ln_img, dt_img)

    # 레시피 리스트를 섞습니다.
    #shuffle(vegan_img)
    #shuffle(hp_img)
    #shuffle(ln_img)
    #shuffle(dt_img)

    return (vegan_img,  hp_img,  ln_img, dt_img)