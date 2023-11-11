from django.urls import path
from .views import menu_detail

urlpatterns = [
    path('menu/<int:FOOD_ID>/', menu_detail, name='menu_detail'),
    # 다른 URL 패턴 추가
]