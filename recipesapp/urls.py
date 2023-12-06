from django.urls import path

from likeapp.views import toggle_like, check_like_status, delete_like
from .views import menu_detail

from . import views
from .views import Predict

# from .views import menu_list
appname='recipesapp'
urlpatterns = [
    #path('menu/<int:food_id>/', menu_detail, name='menu_detail'),
    path('menu/<int:food_id>/like/', toggle_like, name='api_toggle_like'),
    path('menu/<int:food_id>/like-status/', check_like_status, name='api_like_status'),
    path('menu/<int:food_id>/like-delete/', delete_like, name='delete_like'),
    # 다른 URL 패턴 추가
    path('menu/<int:imageId>/<str:category>', menu_detail, name='menu_detail'),
    # path('list/', menu_list, name='menu_list'),
]