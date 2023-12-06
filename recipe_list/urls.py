from django.urls import path
from . import views
from recipesapp.views import menu_detail as other_app_recipe_detail  # 수정이 필요한 부분

urlpatterns = [
    path('recipe_list/', views.recipe_list, name='recipe_list'),

    # 이미 구현된 디테일 뷰 사용
    path('recipe_detail/<int:menu_id>/', other_app_recipe_detail, name='recipe_detail'),
]