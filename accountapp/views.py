from random import shuffle

from django.shortcuts import render
from excel_import.models import FoodModel
def homepage(request):
    data_list = list(FoodModel.objects.values('ATT_FILE_NO_MAIN'))
    shuffle(data_list)
    return render(request, 'accountapp/home.html',{'data_list': data_list})
