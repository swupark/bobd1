from django.urls import path
from .views import menu_detail
from .views import menu_list

urlpatterns = [
    path('menu/<int:FOOD_ID>/', menu_detail, name='menu_detail'),
    path('list/', menu_list, name='menu_list'),
]